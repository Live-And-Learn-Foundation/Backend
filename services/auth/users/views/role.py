from base.views.base import BaseViewSet
from users.models import Role
from users.serializers import RoleSerializer, ShortRoleSerializer

class RoleViewSet(BaseViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    serializer_map = {
        "list": ShortRoleSerializer
    }
    required_alternate_scopes = {
        "create": [["admin:roles:edit"]],
        "update": [["admin:roles:edit"]],
        "destroy": [["admin:roles:edit"]],
        "multiple_delele": [["admin:roles:edit"]],
        "list": [["admin:roles:view"], ["users:view-mine"]],
        "retrieve": [["admin:roles:view"], ["users:view-mine"]],
    }