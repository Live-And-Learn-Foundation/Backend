import uuid
from django.db import models
from base.models import TimeStampedModel


class SubjectMaterial(TimeStampedModel):
    subject_id = models.UUIDField(
        primary_key=False, default=uuid.uuid4, editable=True, unique=False
    )
    title = models.CharField(max_length=100, null=True, blank=True)
    file_path = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    
    class Meta:
        db_table = "subject_materials"
