from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
   path("", views.index, name='main'),
   path("upload/", views.CoverLetterCreated.as_view(), name='upload'),
   path("result_list/", views.CoverLetterList.as_view(), name='result_list'),
   path("howtouse/", views.howtouse, name='howtouse'),
   path("check/", views.spelling_check),
   path("count/", views.characters_count),
   path("detail/", views.detail),
   path("details/", views.details),
]