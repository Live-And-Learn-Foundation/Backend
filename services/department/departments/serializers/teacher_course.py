from rest_framework.fields import UUIDField
from rest_framework import serializers
from departments.models import Teacher, TeacherCourse
from departments.serializers.teacher import TeacherSerializer


class TeacherCourseSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer(required=False)
    teacher_id = serializers.PrimaryKeyRelatedField(required=False, write_only=True, queryset=Teacher.objects.all(),
                                                    pk_field=UUIDField(format='hex'), source='teacher')

    class Meta:
        model = TeacherCourse
        fields = [
            "id",
            "teacher",
            "teacher_id",
            "course_id",
        ]
