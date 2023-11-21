# User 모델

### `member_site/models.py`
```py
class User(AbstractUser):
   birthday =  models.DateField()
   phone = models.CharField(max_length=16)
```
- `AbstractUser`: 장고에서 기본적으로 지원해주는 User을 확장하기 위한 class
   - 기존 장고 User가 가지고 있던 필드 등을 이어받고, 새로운 필드를 추가하여 확장하였음.
- `birthday`: 생일
   - 형식 예시 :2023-11-21
- `phone`: 전화번호

# 장고의 Auth 세팅및 URI 매핑

- `member_site/urls.py`
   ```py
   from django.urls import path
   from django.contrib.auth import views as auth_views
   from . import views

   urlpatterns = [
      path("login/", auth_views.LoginView.as_view(template_name='member/login.html'), name='login'),
      path("logout/", auth_views.LogoutView.as_view(), name='logout'),
      path("join/", views.join, name='join'),
   ]
   ```

# 회원가입

- `member_site/forms.py`
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

- `member_site/views.py`
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

- `templates/member/join.html`
   ```html
   <form method="post" enctype="application/x-www-form-urlencoded">
      {% csrf_token %}
      {{ userForm | crispy }}
      <input type="submit" class="btn btn-primary">
   </form>
   ```

# 로그인
- `templates/member/login.html`
   ```html
   <form method="post">
      {% csrf_token %}
      {{ form | crispy }}
      <input type="submit" class="btn btn-primary">
   </form>
   ```