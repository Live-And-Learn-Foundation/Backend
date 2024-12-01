from rest_framework.fields import UUIDField
from rest_framework import serializers
from departments.models import Teacher, TeacherType,Department
from departments.serializers.teacher_type import TeacherTypeSerializer
from .department import DepartmentSerializer

class TeacherSerializer(serializers.ModelSerializer):
    teacher_type = TeacherTypeSerializer(required=False)
    teacher_type_id = serializers.PrimaryKeyRelatedField(required=False, write_only=True,
                                                         queryset=TeacherType.objects.all(),
                                                         pk_field=UUIDField(format='hex'), source='teacher_type')
    departments = DepartmentSerializer(many=True, required=False)
    department_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        required=False,
        write_only=True,
        queryset=Department.objects.all(),
        source='departments'
    )
    class Meta:
        model = Teacher
        fields = [
            "id",
            "user_id",
            "teacher_type",
            "teacher_type_id",
            "departments",
            "department_ids"
        ]
        
# class ShortTeacherSerializer(serializers.ModelSerializer):
#     teacher_type = TeacherTypeSerializer(required=False)
#     teacher_type_id = serializers.PrimaryKeyRelatedField(required=False, write_only=True,
#                                                          queryset=TeacherType.objects.all(),
#                                                          pk_field=UUIDField(format='hex'), source='teacher_type')
#     # departments = DepartmentSerializer(many=True, required=False)
#     class Meta:
#         model = Teacher
#         fields = [
#             "id",
#             "user_id",
#             "teacher_type",
#             "teacher_type_id",
#             # "departments",
#         ]
