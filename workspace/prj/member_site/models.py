from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError

# 유저
class User(AbstractUser):
   birthday =  models.DateField()
   phone = models.CharField(max_length=16)