from rest_framework.fields import UUIDField
from rest_framework import serializers
from departments.models import Teacher, Department, TeacherDepartment
from departments.serializers.teacher import TeacherSerializer
from departments.serializers.department import DepartmentSerializer


class TeacherDepartmentSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer(required=False)
    teacher_id = serializers.PrimaryKeyRelatedField(required=False, write_only=True, queryset=Teacher.objects.all(),
                                                    pk_field=UUIDField(format='hex'), source='teacher')
    department = DepartmentSerializer(required=False)
    department_id = serializers.PrimaryKeyRelatedField(required=False, write_only=True, queryset=Department.objects.all(),
                                                       pk_field=UUIDField(format='hex'), source='department')

    class Meta:
        model = TeacherDepartment
        fields = [
            "id",
            "teacher",
            "teacher_id",
            "department",
            "department_id",
        ]
