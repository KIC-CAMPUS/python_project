from .models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm 

class UserForm(UserCreationForm):

   username = forms.CharField(label="ID")
   email = forms.EmailField()
   conpany_name = forms.CharField(label="회사명")

   class Meta:
      model = User
      fields = ("username", "conpany_name", "email")