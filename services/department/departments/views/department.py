from base.views.base import BaseViewSet
from departments.models import Department
from departments.serializers import DepartmentSerializer


class DepartmentViewSet(BaseViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    required_alternate_scopes = {
        "create": [["admin:departments:edit"]],
        "update": [["department:edit-mine"], ["admin:departments:edit"]],
        "destroy": [["admin:departments:edit"]],
        "retrieve": [["department:view-mine"], ["admin:departments:view"]],
        "list": [["department:view-mine"], ["admin:departments:view"]],
    }
