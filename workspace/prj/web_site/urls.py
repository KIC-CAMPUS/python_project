from django.urls import path
from . import views

urlpatterns = [
   path("", views.index, name='main'),
   path("howtouse/", views.howtouse, name='howtouse'),
   path("check/", views.spelling_check),
   path("count/", views.characters_count),
]