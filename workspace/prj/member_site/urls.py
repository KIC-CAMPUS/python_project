from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
   path("login/", auth_views.LoginView.as_view(template_name='member/login.html'), name='login'),
   path("logout/", auth_views.LogoutView.as_view(), name='logout'),
   path("join/", views.join, name='join'),
   path("mypage/", views.MypageView.as_view(), name='mypage'),
   path("mypage/delete", views.mypage_coverLetterDelete, name='mypage_coverletter_delete'),
   # 정렬
   path('mypage/sort/<q>/', views.Mypage_CoverLetterSortList.as_view()),
   # 검색
   path('mypage/search/<str:q>/', views.PostSearch.as_view()),

   # 아이디, 비밀번호 찾기 페이지가는 로직
   path('findid/', views.findid, name='findid'),
   path('findpw/', views.findpw, name='findpw'),

   # 아이디, 비밀번호 찾기 확인 로직
   path("id_success/", views.id_check, name='id_success'),
   path("pw_success/", views.pw_check, name='pw_success'),

   # 회원 정보 수정
   path("member/update/", views.update, name='user_update'),
]