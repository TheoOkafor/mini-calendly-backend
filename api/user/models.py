from django.db import models
from django.utils import timezone

class User(models.Model):
  name = models.CharField(max_length=128)
  time_zone = models.CharField(max_length=250, null=True)
  created_at = models.DateTimeField(default=timezone.now)
  modified_at = models.DateTimeField(default=timezone.now)
