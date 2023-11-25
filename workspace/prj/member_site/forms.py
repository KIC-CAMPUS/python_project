from .models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):

   username = forms.CharField(label="ID")
   last_name = forms.CharField(label="닉네임")
   phone = forms.CharField(label="전화번호")
   birthday = forms.DateField(label="생일", widget=forms.TextInput(attrs={'type': 'date'}))

   class Meta:
      model = User
      fields = ("first_name", "last_name",
                "birthday", "phone",
                "username", "password1", "password2",)


class FindUsernameForm(forms.Form):
    first_name = forms.CharField(label="이름")
    phone = forms.CharField(label="전화번호")
    birthday = forms.DateField(label="생일", widget=forms.TextInput(attrs={'type': 'date'}))

class FindpwForm(forms.Form):
    username = forms.CharField(label="아이디")
    first_name = forms.CharField(label="이름")
    phone = forms.CharField(label="전화번호")
    birthday = forms.DateField(label="생일", widget=forms.TextInput(attrs={'type': 'date'}))