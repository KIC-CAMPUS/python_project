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

# 2. 로그인
- `coverletter_site/templates/coverletter_site/login.html`
   ```html
   <form method="post">
      {% csrf_token %}
      {{ form | crispy }}
      <input type="submit" class="btn btn-primary">
   </form>
   ```

# 3. 회원가입

- `coverletter_site/forms.py`
   ```py
   from django import forms
   from django.contrib.auth.models import User
   from django.contrib.auth.forms import UserCreationForm 

   class UserForm(UserCreationForm):

      email = forms.EmailField()

      class Meta:
         model = User
         fields = ("username", "email")
   ```

- `coverletter_site/views.py`
   ```py
   from django.shortcuts import render, redirect
   from .forms import UserForm

   def join(request):
      # POST
      if request.method == "POST":
         form = UserForm(request.POST)
         if form.is_valid():
            form.save()
            print(form)
            return redirect('login')
      # GET
      form = UserForm()
      return render(request, "coverletter_site/join.html", {'userForm':form})
   ```

- `coverletter_site/templates/coverletter_site/join.html`
   ```html
   <form method="post" enctype="application/x-www-form-urlencoded">
      {% csrf_token %}
      {{ userForm | crispy }}
      <input type="submit" class="btn btn-primary">
   </form>
   ```