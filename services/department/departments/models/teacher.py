import uuid
from django.db import models
from base.models import TimeStampedModel
from departments.models.teacher_type import TeacherType


class Teacher(TimeStampedModel):
    user_id = models.UUIDField(
        primary_key=False, default=uuid.uuid4, editable=False, unique=True
    )
    teacher_type = models.ForeignKey(
        TeacherType, on_delete=models.CASCADE, blank=True, related_name="teacher_types")
    class Meta:
        db_table = "teachers"
