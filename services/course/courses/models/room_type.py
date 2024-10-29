from base.models import TimeStampedModel
from django.db import models


class RoomType(TimeStampedModel):
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        db_table = "room_types"
