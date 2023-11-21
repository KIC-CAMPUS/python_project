from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
   path("review_list/", views.review_list, name="review_list"),
   path("review_create/", views.review_create, name="review_create"),
]