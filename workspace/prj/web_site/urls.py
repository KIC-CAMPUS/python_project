from django.urls import path
from . import views

urlpatterns = [
   path("", views.index, name='main'),
   path("howtouse/", views.howtouse, name='howtouse'),
   path("count/", views.characters_count),
   path("check/", views.characters_check),
]