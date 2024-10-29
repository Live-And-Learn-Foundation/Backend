from base.models.timestamped import TimeStampedModel
from django.db import models


class UserDetail(TimeStampedModel):
    date_of_birth = models.DateField(null=True, blank=True)
    degree = models.CharField(max_length=100, null=True, blank=True)
    academic_title = models.CharField(max_length=100, null=True, blank=True)
    biography = models.TextField(null=True, blank=True)

    class Meta:
        db_table = "users_detail"
