from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
   path("", views.index, name='main'),
   path("login/", auth_views.LoginView.as_view(template_name='coverletter_site/login.html'), name='login'),
   path("logout/", auth_views.LogoutView.as_view(), name='logout'),
   path("join/", views.join, name='join'),
   path("upload/", views.CoverLetterCreated.as_view(), name='upload'),
   path("result_list/", views.CoverLetterList.as_view(), name='result_list'),
   path("mypage/", views.mypage, name='mypage'),
   path("howtouse/", views.howtouse, name='howtouse'),
   path("review_list/", views.review_list),
   path("review_create/", views.review_create),
   path("check/", views.spelling_check),
   path("count/", views.characters_count),
]