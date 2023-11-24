from django.urls import path
from . import views

urlpatterns = [
   path("list/", views.ReviewList.as_view(), name="review_list"),
   path("write/", views.ReviewCreated.as_view(), name="review_create"),
   path("<int:pk>/", views.ReviewDetail.as_view(), name="review_detail"),
   path("<int:pk>/edit", views.ReviewEdit.as_view(), name="review_edit"),

   # 화면 볼려고 만들었습니다. 무시하시면 될거 같아요
   path("edit/", views.edit, name="edit"),
]