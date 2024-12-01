from base.views.base import BaseViewSet
from departments.models import Teacher
from departments.serializers import TeacherSerializer
from django.db.models import Q
import requests
from rest_framework.response import Response
from rest_framework import status

class TeacherViewSet(BaseViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

    required_alternate_scopes = {
        "create": [["admin:teachers:edit"]],
        "update": [["teacher:edit-mine"], ["admin:teachers:edit"]],
        "destroy": [["admin:teachers:edit"]],
        "retrieve": [["teacher:view-mine"], ["admin:teachers:view"]],
        "list": [["teacher:view-mine"], ["admin:teachers:view"]],
    }

    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        params = request.query_params

        department_ids = params.get("department_ids")
        print(department_ids)
        if department_ids not in (None, ""):
            print("here")
            department_ids_list = department_ids.split(",")
            queryset = queryset.filter(departments__id__in=department_ids_list)

        teacher_type_ids = params.get("teacher_type_ids")
        if teacher_type_ids:
            teacher_type_ids_list = teacher_type_ids.split(",")
            queryset = queryset.filter(teacher_type__id__in=teacher_type_ids_list)

        # Search by searchQuery
        search_query = params.get("search")
        if search_query and hasattr(self, 'search_map') and self.search_map:
            query = Q()
            for field, op in self.search_map.items():
                kwargs = {f"{field}__{op}": search_query}
                query |= Q(**kwargs)
            queryset = queryset.filter(query)

        teacher_data = []
        user_cache = {}

        for teacher in queryset:
            user_id = teacher.user_id
            if user_id in user_cache:
                # If user data is already cached
                teacher_info = self.get_serializer(teacher).data
                teacher_info['user'] = user_cache[user_id]
            else:
                try:
                    teacher_info = self.get_user(teacher, request)
                    user_cache[user_id] = teacher_info['user']  # Cache user data
                except requests.exceptions.RequestException as e:
                    return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
            teacher_data.append(teacher_info)

        # Paginate or return the full list
        page_size = params.get('page_size')
        if page_size is not None:
            page = self.paginate_queryset(teacher_data)
            return self.get_paginated_response(page)

        return Response(teacher_data, status=status.HTTP_200_OK)

    def get_user(self, teacher, request, *args, **kwargs):
        user_id = teacher.user_id
        # headers = {
        #     'x-api-key': 'YOUR_STATIC_API_KEY'
        # }
        try:
            access_token = request.headers.get('Authorization')
            headers = {'Authorization': access_token}
            response = requests.get(
                f"http://host.docker.internal:9000/api/v1/users/{user_id}",
                headers=headers
            )
            response.raise_for_status()
            user_data = response.json()
            teacher_info = self.get_serializer(teacher).data
            teacher_info['user'] = user_data
            return teacher_info
        except requests.exceptions.RequestException as e:
            raise(e)
        
        
        
# def list(self, request, *args, **kwargs):
    #     queryset = self.filter_queryset(self.get_queryset())
    #     params = request.query_params
    #     ids = params.getlist('ids')
    #     print("ids", ids)
    #     if ids:
    #         queryset = queryset.filter(id__in=ids)

    #     # Fetch teachers list
    #     keyword = params.get("keyword")
    #     if keyword and len(self.search_map) > 0:
    #         query = Q()
    #         for field, op in self.search_map.items():
    #             kwargs = {'{0}__{1}'.format(field, op): keyword}
    #             query |= Q(**kwargs)
    #         queryset = queryset.filter(query)
        
    #     teacher_data = []
    #     user_cache = {}  # Cache for user data
    #     for teacher in queryset:
    #         user_id = teacher.user_id
    #         if user_id in user_cache:
    #             teacher_info = self.get_serializer(teacher).data
    #             teacher_info['user'] = user_cache[user_id]
    #             teacher_data.append(teacher_info)
    #         else:
    #             try:
    #                 teacher_info = self.get_user(teacher, request)
    #                 user_cache[user_id] = teacher_info['user']
    #                 teacher_data.append(teacher_info)
    #             except requests.exceptions.RequestException as e:
    #                 return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)