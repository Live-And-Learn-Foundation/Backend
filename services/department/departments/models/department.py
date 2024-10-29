from django.db import models
from base.models import TimeStampedModel


class Department(TimeStampedModel):
    more_info = models.JSONField(null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    department_type = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = "departments"
