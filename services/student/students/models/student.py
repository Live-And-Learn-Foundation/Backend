import uuid
from django.db import models
from base.models import TimeStampedModel


class Student(TimeStampedModel):
    user_id = models.UUIDField(
        primary_key=False, default=uuid.uuid4, editable=True, unique=False
    )
    enrollment_year = models.DateField(null=True, blank=True)

    class Meta:
        db_table = "students"
