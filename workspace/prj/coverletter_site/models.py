from django.db import models

from django.db import models
from django.contrib.auth.models import AbstractUser

# 유저
class User(AbstractUser):
   conpany_name = models.TextField(max_length=100, null=True)

# 자소서
class CoverLetter(models.Model):
   company = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
   title = models.CharField(max_length=100)
   content = models.TextField(max_length=500)
   status = models.BooleanField()
   
   create_at = models.DateTimeField(auto_now_add=True)

   def __str__(self) -> str:
      return f'[{self.pk}] {self.title}'