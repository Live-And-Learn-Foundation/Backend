from base.views.base import BaseViewSet
from students.models import Student
from students.serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
import requests


class StudentViewSet(BaseViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    required_alternate_scopes = {
        "create": [["admin:students:edit"]],
        "update": [["student:edit-mine"], ["admin:students:edit"]],
        "destroy": [["admin:students:edit"]],
        "retrieve": [["student:view-mine"], ["admin:students:view"]],
        "list": [["student:view-mine"], ["admin:students:view"]],
    }

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        params = request.query_params

        # Fetch students list
        keyword = params.get("keyword")
        if keyword and len(self.search_map) > 0:
            query = Q()
            for field, op in self.search_map.items():
                kwargs = {'{0}__{1}'.format(field, op): keyword}
                query |= Q(**kwargs)
            queryset = queryset.filter(query)

        # Fetch user data for each student
        student_data = []
        for student in queryset:
            try:
                student_info = self.get_user(student, request)
                student_data.append(student_info)
            except requests.exceptions.RequestException as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        # Paginate or return the full list
        if params.get('page_size') is not None:
            page = self.paginate_queryset(student_data)
            return self.get_paginated_response(page)
        else:
            return Response(student_data, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        student = self.get_object()
        try:
            student_info = self.get_user(student, request)
            return Response(student_info)
        except requests.exceptions.RequestException as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def get_user(self, student, request, *args, **kwargs):
        user_id = student.user_id
        try:
            # Extract access token from request headers
            access_token = request.headers.get('Authorization')
            headers = {'Authorization': access_token}
            response = requests.get(
                f"http://host.docker.internal:9000/api/auth/v1/users/{user_id}",
                headers=headers
            )
            response.raise_for_status()
            user_data = response.json()
            student_info = self.get_serializer(student).data
            # Add user data to student info
            student_info['user'] = user_data
            return student_info
        except requests.exceptions.RequestException as e:
            raise e
