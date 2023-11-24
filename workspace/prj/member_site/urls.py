from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
   path("login/", auth_views.LoginView.as_view(template_name='member/login.html'), name='login'),
   path("logout/", auth_views.LogoutView.as_view(), name='logout'),
   path("join/", views.join, name='join'),
   path("mypage/", views.mypage, name='mypage'),
   path("findid/", views.findid, name='findid'),
   path("findpassword/", views.findpassword, name='findpassword'),
   path("id_success/", views.id_success, name='id_success'),
   path("pw_success/", views.pw_success, name='pw_success'),
   path("findid_/", views.findid_, name='findid_'),
   path("findpw_/", views.findpw_, name='findpw_'),
]