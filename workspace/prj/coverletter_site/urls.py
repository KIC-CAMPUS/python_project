from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
   path("", views.index, name='main'),
   path("upload/", views.CoverLetterCreated.as_view(), name='upload'),
   path("result_list/", views.CoverLetterList.as_view(), name='result_list'),
   path("detail/", views.CoverLetterResultList.as_view(), name='detail_list'),
   path("detail/<int:pk>/", views.CoverLetterDetail.as_view(), name='detail_detail'),
   path("howtouse/", views.howtouse, name='howtouse'),
   path("check/", views.spelling_check),
   path("count/", views.characters_count),
]