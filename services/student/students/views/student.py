from base.views.base import BaseViewSet
from students.models import Student
from students.serializers import StudentSerializer


class StudentViewSet(BaseViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    required_alternate_scopes = {
        "create": [["admin:students:edit"]],
        "update": [["student:edit-mine"], ["admin:students:edit"]],
        "destroy": [["admin:students:edit"]],
        "retrieve": [["student:view-mine"], ["admin:students:view"]],
        "list": [["student:view-mine"], ["admin:students:view"]],
    }