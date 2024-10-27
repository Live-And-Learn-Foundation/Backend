from django.db import models
from base.models import TimeStampedModel


class TeacherType(TimeStampedModel):
    name = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = "teacher_types"
