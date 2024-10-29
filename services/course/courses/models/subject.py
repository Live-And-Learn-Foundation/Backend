import uuid

from base.models import TimeStampedModel
from django.db import models


class Subject(TimeStampedModel):
    major_id = models.UUIDField(
        primary_key=False, default=uuid.uuid4, editable=True, unique=False
    )
    title = models.CharField(max_length=100, null=True, blank=True)
    credit = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = "subjects"
