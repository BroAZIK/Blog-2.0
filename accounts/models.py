from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    firstname = models.CharField(max_length=30, blank=True, null=True)
    lastname = models.CharField(max_length=30, blank=True, null=True)

    age  = models.PositiveIntegerField(null=True, blank=True)