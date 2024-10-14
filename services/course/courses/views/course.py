from base.views.base import BaseViewSet
from courses.models import Course
from courses.serializers import CourseSerializer


class CourseViewSet(BaseViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    required_alternate_scopes = {
        "create": [["admin:courses:edit"]],
        "update": [["course:edit-mine"], ["admin:courses:edit"]],
        "destroy": [["admin:courses:edit"]],
        "retrieve": [["course:view-mine"], ["admin:courses:view"]],
        "list": [["course:view-mine"], ["admin:courses:view"]],
    }
