from django.db import models
from base.models import TimeStampedModel
from courses.models.room_type import RoomType


class Room(TimeStampedModel):
    room_type = models.ForeignKey(
        RoomType, on_delete=models.CASCADE, blank=True, related_name="room_types")
    title = models.CharField(max_length=100, null=True, blank=True)
    capacity = models.IntegerField(null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = "rooms"
