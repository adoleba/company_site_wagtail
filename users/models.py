from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models


SEX_CHOICES = (
    ('K', 'Kobieta'),
    ('M', 'Mężczyzna'),
)


class User(AbstractUser):
    country = models.CharField(max_length=255, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, blank=True, null=True,)
    about = models.TextField(blank=True, null=True)
