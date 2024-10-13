from rest_framework.fields import UUIDField
from rest_framework import serializers
from students.models import StudentCourse, Student
from students.serializers.student import StudentSerializer

class StudentCourseSerializer(serializers.ModelSerializer):
    student = StudentSerializer(required=False)
    student_id = serializers.PrimaryKeyRelatedField(required=False, write_only=True, queryset=Student.objects.all(),
                                                 pk_field=UUIDField(format='hex'), source='student')

    class Meta:
        model = StudentCourse
        fields = [
            "id",
            "student",
            "student_id",
            "course_id",
            "title",
            "enrollment_date",
        ]
