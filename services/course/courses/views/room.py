from base.views.base import BaseViewSet
from courses.models import Room
from courses.serializers import RoomSerializer


class RoomViewSet(BaseViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    required_alternate_scopes = {
        "create": [["admin:rooms:edit"]],
        "update": [["room:edit-mine"], ["admin:rooms:edit"]],
        "destroy": [["admin:rooms:edit"]],
        "retrieve": [["room:view-mine"], ["admin:rooms:view"]],
        "list": [["room:view-mine"], ["admin:rooms:view"]],
    }
