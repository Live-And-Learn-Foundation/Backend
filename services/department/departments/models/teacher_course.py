import uuid
from django.db import models
from base.models import TimeStampedModel
from departments.models.teacher import Teacher


class TeacherCourse(TimeStampedModel):
    course_id = models.UUIDField(
        primary_key=False, default=uuid.uuid4, editable=True, unique=False
    )
    teacher = models.ForeignKey(
        Teacher, on_delete=models.CASCADE, blank=True, related_name="teachers_teacher_course")

    class Meta:
        db_table = "teacher_courses"
