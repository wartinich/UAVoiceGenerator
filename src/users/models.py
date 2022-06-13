from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Customize User"""
    SEX = [
        ('male', 'Male'),
        ('female', 'Female')
    ]

    first_name = models.CharField(verbose_name='First name', max_length=25)
    last_name = models.CharField(verbose_name='Last name', max_length=40)
    email = models.EmailField(verbose_name='Email', max_length=150, unique=True)
    avatar_image = models.ImageField(verbose_name='Avatar', upload_to='avatars/')
    birth_date = models.DateField(verbose_name='Birth date')
    sex = models.CharField(verbose_name='Sex', choices=SEX, max_length=7)

    REQUIRED_FIELDS = ['email',]