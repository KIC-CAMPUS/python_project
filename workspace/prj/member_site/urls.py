from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
   path("login/", auth_views.LoginView.as_view(template_name='member/login.html'), name='login'),
   path("logout/", auth_views.LogoutView.as_view(), name='logout'),
   path("join/", views.join, name='join'),
   path("mypage/", views.mypage, name='mypage'),

   # 페이지 볼려고 추가했습니다. 무시하셔도 될거 같아요
   path("mypage/edit/", views.mypage_edit, name='mypage_edit'),
]