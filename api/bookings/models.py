from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

class Bookings(models.Model):
  user_id = models.CharField(max_length=50, null=False)
  mentor_id = models.ForeignKey(
    get_user_model(),
    related_name='mentor',
    on_delete=models.CASCADE,
    null=True,
    blank=True,
    default=1
  )
  date_time = models.CharField(max_length=250, null=False)
  created_at = models.DateTimeField(default=timezone.now)
  modified_at = models.DateTimeField(default=timezone.now)
