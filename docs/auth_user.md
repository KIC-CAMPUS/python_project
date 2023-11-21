# 1. 장고의 Auth 세팅및 URI 매핑

- `coverletter_site/urls.py`
   ```py
   from django.urls import path
   from django.contrib.auth import views as auth_views
   from . import views

   urlpatterns = [
      path("login/", auth_views.LoginView.as_view(template_name='coverletter_site/login.html'), name='login'),
      path("logout/", auth_views.LogoutView.as_view(), name='logout'),
      path("join/", views.join, name='join'),
   ]
   ```

- `config/settings.py`
   ```py
   INSTALLED_APPS = [
      'django.contrib.auth',
      #...
   ]
   
   LOGOUT_REDIRECT_URL = "/"
   ```

# 2. 회원가입

- `coverletter_site/models.py`
   ```py
   from django.db import models
   from django.contrib.auth.models import AbstractUser
   
   class User(AbstractUser):
      birthday =  models.DateField()
      phone = models.CharField(max_length=16)
   ```

- `coverletter_site/forms.py`
   ```py
   from django import forms
   from .models import User
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
   ```

- `coverletter_site/views.py`
   ```py
   from django.shortcuts import render, redirect
   from .models import User
   from .forms import UserForm

   def join(request):
      # POST
      if request.method == "POST":
         form = UserForm(request.POST)
         if form.is_valid():
            join_user = form.save()
            login(request, join_user)
            return render(request, "coverletter_site/join_success.html")
      # GET
      else :
         form = UserForm()
      return render(request, "coverletter_site/join.html", {'form': form})
   ```

- `coverletter_site/templates/coverletter_site/join.html`
   ```html
   <form method="post" enctype="application/x-www-form-urlencoded">
      {% csrf_token %}
      {{ userForm | crispy }}
      <input type="submit" class="btn btn-primary">
   </form>
   ```

# 3. 로그인
- `coverletter_site/templates/coverletter_site/login.html`
   ```html
   <form method="post">
      {% csrf_token %}
      {{ form | crispy }}
      <input type="submit" class="btn btn-primary">
   </form>
   ```