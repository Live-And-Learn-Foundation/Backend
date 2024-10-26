from rest_framework import serializers
from departments.models import Department


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = [
            "id",
            "more_info",
            "name",
            "description",
            "department_type",
        ]
