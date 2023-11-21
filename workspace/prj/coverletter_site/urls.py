from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
   path("", views.index, name='main'),
   path("login/", auth_views.LoginView.as_view(template_name='coverletter_site/login.html'), name='login'),
   path("logout/", auth_views.LogoutView.as_view(), name='logout'),
   path("join/", views.join, name='join'),
   path("upload/", views.coverletter_upload, name='upload'),
   path("result_list/", views.CoverLetterList.as_view(), name='result_list'),
   path("mypage/", views.mypage),

   # 화면 확인용으로 임시로 만들었습니다. 편하신대로 바꾸시면 될 것 같습니다.
   path("review_list/", views.review_list),
   path("review_create/", views.review_create),
   path("check/", views.check),
   path("count/", views.count),
]