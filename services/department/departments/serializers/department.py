from rest_framework import serializers
from departments.models import Department
from .major import MajorSerializer
class DepartmentSerializer(serializers.ModelSerializer):
    majors = MajorSerializer(many = True, required=False)
    class Meta:
        model = Department
        fields = [
            "id",
            "more_info",
            "name",
            "description",
            "department_type",
            # "departments_major",
            "majors"
        ]
