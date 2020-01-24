from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

class Openings(models.Model):
  owner = models.ForeignKey(
    get_user_model(),
    related_name='owner',
    on_delete=models.CASCADE,
    null=True,
    blank=True,
    default=1
  )
  date_time = models.CharField(max_length=250, null=True)
  created_at = models.DateTimeField(default=timezone.now)
  modified_at = models.DateTimeField(default=timezone.now)
