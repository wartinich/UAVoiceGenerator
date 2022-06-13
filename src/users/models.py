from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """Customize User"""
    phone_number = models.CharField(verbose_name='Phone number', max_length=13)