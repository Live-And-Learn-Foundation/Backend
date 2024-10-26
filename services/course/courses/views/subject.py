from base.views.base import BaseViewSet
from courses.models import Subject
from courses.serializers import SubjectSerializer


class SubjectViewSet(BaseViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

    required_alternate_scopes = {
        "create": [["admin:subjects:edit"]],
        "update": [["subject:edit-mine"], ["admin:subjects:edit"]],
        "destroy": [["admin:subjects:edit"]],
        "retrieve": [["subject:view-mine"], ["admin:subjects:view"]],
        "list": [["subject:view-mine"], ["admin:subjects:view"]],
    }
