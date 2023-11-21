from django.db import models
from django.contrib.auth.models import AbstractUser

# 유저
class User(AbstractUser):
   birthday =  models.DateField()
   phone = models.CharField(max_length=16)

# 자소서
class CoverLetter(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
   document_type = models.CharField(max_length=100, choices=[('1', 'A'), ('2', 'B'), ('3', 'C'), ('4', 'D')])
   content = models.TextField(blank=True)
   document_file = models.FileField(upload_to="documents/%Y/%m/%d/", null=True)
   
   rate = models.DecimalField(max_digits=2, decimal_places=1, null=True)
   create_at = models.DateTimeField(auto_now_add=True)

   def __str__(self) -> str:
      return f'[{self.pk}] {self.document_type} :: {self.user}'