from base.views.base import BaseViewSet
from departments.models import TeacherType
from departments.serializers import TeacherTypeSerializer


class TeacherTypeViewSet(BaseViewSet):
    queryset = TeacherType.objects.all()
    serializer_class = TeacherTypeSerializer

    required_alternate_scopes = {
        "create": [["admin:teachers:edit"]],
        "update": [["teacher:edit-mine"], ["admin:teachers:edit"]],
        "destroy": [["admin:teachers:edit"]],
        "retrieve": [["teacher:view-mine"], ["admin:teachers:view"]],
        "list": [["teacher:view-mine"], ["admin:teachers:view"]],
    }
