from .models import *
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm 

class UserForm(UserChangeForm):

   email = forms.EmailField()

   class Mata:
      model = User
      fields = ["username", "email"]