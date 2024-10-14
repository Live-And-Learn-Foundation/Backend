from django.db import models
from base.models import TimeStampedModel
from departments.models.teacher import Teacher
from departments.models.department import Department

class TeacherDepartment(TimeStampedModel):
    teacher = models.ForeignKey(
        Teacher, on_delete=models.CASCADE, blank=True, related_name="teachers")
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, blank=True, related_name="departments_teacher_department")
    class Meta:
        db_table = "teacher_departments"
