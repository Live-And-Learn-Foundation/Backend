from rest_framework.fields import UUIDField
from rest_framework import serializers
from departments.models import Department, Major


class MajorSerializer(serializers.ModelSerializer):
    department = serializers.SerializerMethodField()
    department_id = serializers.PrimaryKeyRelatedField(
        required=False,
        write_only=True,
        queryset=Department.objects.all(),
        pk_field=UUIDField(format='hex'),
        source='department'
    )

    def get_department(self, obj):
        from .department import DepartmentSerializer  # Import inside the method to avoid circular import
        if obj.department:
            return DepartmentSerializer(obj.department).data
        return None

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
