from base.views.base import BaseViewSet
from documents.models import Thesis
from documents.serializers import ThesisSerializer


class ThesisViewSet(BaseViewSet):
    queryset = Thesis.objects.all()
    serializer_class = ThesisSerializer

    required_alternate_scopes = {
        "create": [["admin:thesis:edit"]],
        "update": [["thesis:edit-mine"], ["admin:thesis:edit"]],
        "destroy": [["admin:thesis:edit"]],
        "retrieve": [["thesis:view-mine"], ["admin:thesis:view"]],
        "list": [["thesis:view-mine"], ["admin:thesis:view"]],
    }
