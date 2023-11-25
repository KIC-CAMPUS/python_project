from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
   path("login/", auth_views.LoginView.as_view(template_name='member/login.html'), name='login'),
   path("logout/", auth_views.LogoutView.as_view(), name='logout'),
   path("join/", views.join, name='join'),
   path("mypage/", views.MypageView.as_view(), name='mypage'),
   path("mypage/delete", views.mypage_coverLetterDelete, name='mypage_coverletter_delete'),
   # 페이지 볼려고 추가했습니다. 무시하셔도 될거 같아요
   # 정렬
   path('mypage/sort/<q>/', views.Mypage_CoverLetterSortList.as_view()),
   # 검색
   path('mypage/search/<str:q>/', views.PostSearch.as_view()),
   
   path("findid/", views.findid, name='findid'),
   path("findpw/", views.findpw, name='findpw'),
   #회원 정보 수정
   path("member/update/", views.update, name='user_update'),
]