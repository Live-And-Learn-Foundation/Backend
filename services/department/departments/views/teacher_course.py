from base.views.base import BaseViewSet
from departments.models import TeacherCourse
from departments.serializers import TeacherCourseSerializer


class TeacherCourseViewSet(BaseViewSet):
    queryset = TeacherCourse.objects.all()
    serializer_class = TeacherCourseSerializer

    required_alternate_scopes = {
        "create": [["admin:teachers:edit"]],
        "update": [["teacher:edit-mine"], ["admin:teachers:edit"]],
        "destroy": [["admin:teachers:edit"]],
        "retrieve": [["teacher:view-mine"], ["admin:teachers:view"]],
        "list": [["teacher:view-mine"], ["admin:teachers:view"]],
    }
