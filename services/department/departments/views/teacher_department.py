from base.views.base import BaseViewSet
from departments.models import TeacherDepartment
from departments.serializers import TeacherDepartmentSerializer


class TeacherDepartmentViewSet(BaseViewSet):
    queryset = TeacherDepartment.objects.all()
    serializer_class = TeacherDepartmentSerializer

    required_alternate_scopes = {
        "create": [["admin:teachers:edit"]],
        "update": [["teacher:edit-mine"], ["admin:teachers:edit"]],
        "destroy": [["admin:teachers:edit"]],
        "retrieve": [["teacher:view-mine"], ["admin:teachers:view"]],
        "list": [["teacher:view-mine"], ["admin:teachers:view"]],
    }
