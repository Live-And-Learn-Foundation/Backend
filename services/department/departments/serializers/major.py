from rest_framework.fields import UUIDField
from rest_framework import serializers
from departments.models import Department, Major
from departments.serializers.department import DepartmentSerializer


class MajorSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(required=False)
    department_id = serializers.PrimaryKeyRelatedField(required=False, write_only=True, queryset=Department.objects.all(),
                                                       pk_field=UUIDField(format='hex'), source='department')
    class Meta:
        model = Major
        fields = [
            "id",
            "department",
            "department_id",
            "name",
            "more_info",
            "description",
        ]
