from django.urls import path
from . import views

urlpatterns = [
   path("list/", views.ReviewList.as_view(), name="review_list"),
   path("write/", views.ReviewCreated.as_view(), name="review_create"),
   path("<int:pk>/", views.ReviewDetail.as_view(), name="review_detail"),
   path('<int:pk>/edit/', views.ReviewUpdateView.as_view(), name='review_edit'),
   path('<int:pk>/comment/', views.add_comment, name='add_comment'),
   path('comment/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
]