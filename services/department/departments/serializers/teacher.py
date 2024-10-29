from rest_framework.fields import UUIDField
from rest_framework import serializers
from departments.models import Teacher, TeacherType
from departments.serializers.teacher_type import TeacherTypeSerializer


class TeacherSerializer(serializers.ModelSerializer):
    teacher_type = TeacherTypeSerializer(required=False)
    teacher_type_id = serializers.PrimaryKeyRelatedField(required=False, write_only=True,
                                                         queryset=TeacherType.objects.all(),
                                                         pk_field=UUIDField(format='hex'), source='teacher_type')

    class Meta:
        model = Teacher
        fields = [
            "id",
            "user_id",
            "teacher_type",
            "teacher_type_id"
        ]
