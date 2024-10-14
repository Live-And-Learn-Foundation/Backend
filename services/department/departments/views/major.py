from base.views.base import BaseViewSet
from departments.models import Major
from departments.serializers import MajorSerializer


class MajorViewSet(BaseViewSet):
    queryset = Major.objects.all()
    serializer_class = MajorSerializer

    required_alternate_scopes = {
        "create": [["admin:departments:edit"]],
        "update": [["department:edit-mine"], ["admin:departments:edit"]],
        "destroy": [["admin:departments:edit"]],
        "retrieve": [["department:view-mine"], ["admin:departments:view"]],
        "list": [["department:view-mine"], ["admin:departments:view"]],
    }
