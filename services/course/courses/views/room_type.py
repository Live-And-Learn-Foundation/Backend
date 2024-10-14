from base.views.base import BaseViewSet
from courses.models import RoomType
from courses.serializers import RoomTypeSerializer


class RoomTypeViewSet(BaseViewSet):
    queryset = RoomType.objects.all()
    serializer_class = RoomTypeSerializer

    required_alternate_scopes = {
        "create": [["admin:rooms:edit"]],
        "update": [["room:edit-mine"], ["admin:rooms:edit"]],
        "destroy": [["admin:rooms:edit"]],
        "retrieve": [["room:view-mine"], ["admin:rooms:view"]],
        "list": [["room:view-mine"], ["admin:rooms:view"]],
    }
