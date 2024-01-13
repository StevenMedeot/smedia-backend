from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.
class User(AbstractBaseUser):
    username = models.CharField("username", unique=True, blank=False, null=False, max_length=255)
    display_name = models.CharField("DisplayName", blank=False, null=False, max_length=255)

    USERNAME_FIELD = 'username'