from django.db import models
from django.utils import timezone
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)

class User(AbstractBaseUser, PermissionsMixin):
  name = models.CharField(max_length=128)
  username = models.CharField(max_length=128, unique=True)
  time_zone = models.CharField(max_length=250, null=True)
  created_at = models.DateTimeField(default=timezone.now)
  modified_at = models.DateTimeField(default=timezone.now)

  REQUIRED_FIELDS = ['time_zone']
  USERNAME_FIELD = 'username'