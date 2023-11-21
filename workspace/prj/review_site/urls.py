from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
   path("review_list/", views.ReviewList.as_view(), name="review_list"),
   path("review_create/", views.ReviewCreated.as_view(), name="review_create"),
]