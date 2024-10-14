from base.views.base import BaseViewSet
from departments.models import Teacher
from departments.serializers import TeacherSerializer


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
