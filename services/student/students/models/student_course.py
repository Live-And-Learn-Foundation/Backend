import uuid
from django.db import models
from base.models import TimeStampedModel
from students.models import Student

class StudentCourse(TimeStampedModel):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, blank=True, related_name="students")
    course_id = models.UUIDField(
        primary_key=False, default=uuid.uuid4, editable=True, unique=False
    )
    title = models.CharField(max_length=100, null=True, blank=True)
    enrollment_date = models.DateField(null=True, blank=True)
    
    class Meta:
        db_table = "student_courses"
