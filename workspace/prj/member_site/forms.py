from django.contrib.auth.hashers import check_password

from .models import User
from django import forms
from django.forms import PasswordInput
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

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

# 회원 정보 수정
class UpdateForm(UserChangeForm):
    first_name = forms.CharField(label="이름", widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    username = forms.CharField(label="ID", widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    last_name = forms.CharField(label="닉네임")
    phone = forms.CharField(label="전화번호")
    birthday = forms.DateField(label="생일", widget=forms.TextInput(attrs={'type': 'date'}))

    class Meta(UserChangeForm.Meta):
        model = User
        fields = ("first_name", "username",
                "last_name",
                "birthday", "phone",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].help_text = "비밀번호를 재설정 해주세요."
        self.fields['password'].widget = PasswordInput(attrs={'placeholder': ''})


class CheckPasswordForm(forms.Form):
    password = forms.CharField(label='비밀번호', widget=forms.PasswordInput(
        attrs={'class': 'form-control', }),
                               )

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = self.user.password

        if password:
            if not check_password(password, confirm_password):
                self.add_error('password', '비밀번호가 일치하지 않습니다.')
