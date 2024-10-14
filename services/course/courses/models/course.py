import uuid
from django.db import models
from base.models import TimeStampedModel
from courses.models.room import Room


class Course(TimeStampedModel):
    subject_id = models.UUIDField(
        primary_key=False, default=uuid.uuid4, editable=False, unique=True
    )
    room = models.ForeignKey(
        Room, on_delete=models.CASCADE, blank=True, related_name="rooms")
    title = models.CharField(max_length=100, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    class Meta:
        db_table = "courses"
