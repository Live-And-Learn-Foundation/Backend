from base.views.base import BaseViewSet
from students.models import StudentCourse
from students.serializers import StudentCourseSerializer


class StudentCourseViewSet(BaseViewSet):
    queryset = StudentCourse.objects.all()
    serializer_class = StudentCourseSerializer
    
    required_alternate_scopes = {
        "create": [["admin:students:edit"]],
        "update": [["student:edit-mine"], ["admin:students:edit"]],
        "destroy": [["admin:students:edit"]],
        "retrieve": [["student:view-mine"], ["admin:students:view"]],
        "list": [["student:view-mine"], ["admin:students:view"]],
    }