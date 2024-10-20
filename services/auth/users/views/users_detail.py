from base.views.base import BaseViewSet
from users.models import UserDetail
from users.serializers import UserDetailSerializer


class UserDetailViewSet(BaseViewSet):
    queryset = UserDetail.objects.all()
    serializer_class = UserDetailSerializer
    
    required_alternate_scopes = {
        "create": [["admin:users:edit"]],
        "update": [["user:edit-mine"], ["admin:users:edit"]],
        "destroy": [["admin:users:edit"]],
        "retrieve": [["user:view-mine"], ["admin:users:view"]],
        "list": [["user:view-mine"], ["admin:users:view"]],
    }