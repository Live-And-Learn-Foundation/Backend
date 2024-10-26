from base.views.base import BaseViewSet
from documents.models import SubjectMaterial
from documents.serializers import SubjectMaterialSerializer


class SubjectMaterialViewSet(BaseViewSet):
    queryset = SubjectMaterial.objects.all()
    serializer_class = SubjectMaterialSerializer

    required_alternate_scopes = {
        "create": [["admin:subject-materials:edit"]],
        "update": [["subject-material:edit-mine"], ["admin:subject-materials:edit"]],
        "destroy": [["admin:subject-materials:edit"]],
        "retrieve": [["subject-material:view-mine"], ["admin:subject-materials:view"]],
        "list": [["subject-material:view-mine"], ["admin:subject-materials:view"]],
    }
