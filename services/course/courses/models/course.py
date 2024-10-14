import uuid
from django.db import models
from base.models import TimeStampedModel
from courses.models.room import Room
from courses.models.subject import Subject


class Course(TimeStampedModel):
    subject = models.ForeignKey(
        Subject, on_delete=models.CASCADE, blank=True, related_name="subjects")
    room = models.ForeignKey(
        Room, on_delete=models.CASCADE, blank=True, related_name="rooms")
    title = models.CharField(max_length=100, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    class Meta:
        db_table = "courses"
