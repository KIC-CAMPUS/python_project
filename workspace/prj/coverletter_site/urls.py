from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
   path("", views.index, name='main'),
   path("login/", auth_views.LoginView.as_view(template_name='coverletter_site/login.html'), name='login'),
   path("logout/", auth_views.LogoutView.as_view(), name='logout'),
   path("join/", views.join, name='join'),
   path("upload/", views.coverletter_upload, name='upload'),
   path("result_list", views.CoverLetterList.as_view(), name='result_list'),
]