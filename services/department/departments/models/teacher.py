import uuid
from django.db import models
from base.models import TimeStampedModel
from departments.models.teacher_type import TeacherType
from .department import Department

class Teacher(TimeStampedModel):
    user_id = models.UUIDField(
        primary_key=False, default=uuid.uuid4, editable=True, unique=False
    )
    teacher_type = models.ForeignKey(
        TeacherType, on_delete=models.CASCADE, blank=True, related_name="teacher_types")
    
    departments = models.ManyToManyField(Department, through='TeacherDepartment', related_name='teachers')
    class Meta:
        db_table = "teachers"
