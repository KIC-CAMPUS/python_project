from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
   path("upload/", views.CoverLetterCreated.as_view(), name='upload'),
   path("list/", views.CoverLetterList.as_view(), name='result_list'),
   path("<int:pk>/", views.CoverLetterDetail.as_view(), name='coverletter_detail'),
   path("delete/", views.coverLetterDelete, name='cover_letter_delete'),
   path('list/search/<str:q>/', views.PostSearch.as_view()),
   path('list/sort/<q>/', views.CoverLetterSortList.as_view()),
   path("list/", views.CoverLetterSortList.as_view(), name=''),
   path('like/', views.coverletter_bookmark, name='coverletter_like'),
]