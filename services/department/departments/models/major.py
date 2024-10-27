from django.db import models
from base.models import TimeStampedModel
from departments.models.department import Department


class Major(TimeStampedModel):
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, blank=True, related_name="departments_major")
    name = models.CharField(max_length=100, null=True, blank=True)
    more_info = models.JSONField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        db_table = "majors"
