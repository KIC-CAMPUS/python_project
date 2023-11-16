from django.urls import path
from . import views

urlpatterns = [
   path("", views.index, name='main'),
   path("login/", views.login, name='login'),
   path("upload/", views.coverletter_upload, name='upload'),
   path("result_list", views.CoverLetterList.as_view(), name='result_list'),
]