from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import check_password

from .models import User
from django import forms

from django.forms import PasswordInput
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm

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

# 비밀번호 재설정
class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(CustomPasswordChangeForm, self).__init__(*args, **kwargs)
        self.fields['old_password'].label = '기존 비밀번호'
        self.fields['old_password'].widget.attrs.update({
            'class': 'form-control',
            'autofocus': False,
        })
        self.fields['new_password1'].label = '새 비밀번호'
        self.fields['new_password1'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['new_password2'].label = '새 비밀번호 확인'
        self.fields['new_password2'].widget.attrs.update({
            'class': 'form-control',
        })

    def clean(self):
        cleaned_data = super(CustomPasswordChangeForm, self).clean()

        old_password = cleaned_data.get('old_password')
        new_password1 = cleaned_data.get('new_password1')
        new_password2 = cleaned_data.get('new_password2')

        # Check if the old password is correct
        user = self.user
        if not user.check_password(old_password):
            raise ValidationError("기존 비밀번호가 올바르지 않습니다.", code='invalid_old_password')

        # Check if the new password is different from the old password
        if old_password == new_password1:
            raise ValidationError("새 비밀번호는 기존 비밀번호와 달라야 합니다.", code='same_as_old_password')

        # Check if the new password and confirmation match
        if new_password1 != new_password2:
            raise ValidationError("새 비밀번호와 확인이 일치하지 않습니다.", code='password_mismatch')

        # Check if the new password has at least 8 characters
        if len(new_password1) < 8:
            raise ValidationError("비밀번호가 너무 짧습니다. 최소 8 문자를 포함해야 합니다.", code='password_too_short')

        # Check if the new password contains at least one non-digit character
        if new_password1.isdigit():
            raise ValidationError("비밀번호가 전부 숫자로 되어 있습니다.", code='password_all_digits')

        return cleaned_data

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
