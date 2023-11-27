from django.contrib import auth, messages
from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect
from django.contrib.auth import login, get_user_model, authenticate
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView

from .forms import UserForm
from .forms import FindUsernameForm
from .forms import FindpwForm
from coverletter_site.views import CoverLetterList, coverLetterDelete

from coverletter_site.models import CoverLetter

# 회원가입
def join(request):
   # POST
   if request.method == "POST":
      form = UserForm(request.POST)
      if form.is_valid():
         join_user = form.save()
         login(request, join_user)
         return render(request, "member/join_success.html")
   # GET
   else :
      form = UserForm()
   return render(request, "member/join.html", {'form': form})

#아이디 찾기
def id_check(request):
   form = FindUsernameForm()
   username = None

   if request.method == "POST":
      form = FindUsernameForm(request.POST)
      if form.is_valid():
         first_name = form.cleaned_data['first_name']
         phone = form.cleaned_data['phone']
         birthday = form.cleaned_data['birthday']

         try:
            user = get_user_model().objects.get(first_name=first_name, phone=phone, birthday=birthday)
            print(f"Username found: {user.username}")
            username = user.username
         except ObjectDoesNotExist as e:
            print(f"ObjectDoesNotExist exception: {e}")
            username = "일치하는 사용자가 없습니다."

   return render(request, "member/id_success.html", {'form': form, 'username': username})

def pw_check(request):
   form = FindpwForm()
   password1 = None

   if request.method == "POST":
      form = FindpwForm(request.POST)
      if form.is_valid():
         username = form.cleaned_data['username']
         first_name = form.cleaned_data['first_name']
         phone = form.cleaned_data['phone']
         birthday = form.cleaned_data['birthday']

         try:
            user = get_user_model().objects.get(username=username, first_name=first_name, phone=phone, birthday=birthday)

         except ObjectDoesNotExist as e:
            print(f"ObjectDoesNotExist exception: {e}")
            password1 = "null"

   return render(request, "member/pw_success.html", {'form': form, 'password1': password1})

class MypageView(CoverLetterList):
   template_name = "member/mypage.html"

   def get_queryset(self):
      return super().get_queryset().filter(bookmark=True)

   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      user = self.request.user
      # Calculate bookmark counts
      context['document_type_1_count'] = CoverLetter.objects.filter(document_type=1, user=user).count()
      context['document_type_2_count'] = CoverLetter.objects.filter(document_type=2, user=user).count()
      context['document_type_3_count'] = CoverLetter.objects.filter(document_type=3, user=user).count()
      context['document_type_4_count'] = CoverLetter.objects.filter(document_type=4, user=user).count()
      context['document_type_5_count'] = CoverLetter.objects.filter(document_type=5, user=user).count()

      return context

# 페이지 볼려고 추가했습니다. 무시하셔도 될거 같아요
# 마이페이지 수정
def mypage_edit(request):
   return render(request, "member/mypage_edit.html")

def mypage_coverLetterDelete(request):
   coverLetterDelete(request)
   return redirect(reverse_lazy('mypage'))

# 검색
class PostSearch(MypageView):
   def get_queryset(self):
      q = self.kwargs['q']
      post_list = super().get_queryset().filter(
         Q(title__contains=q)
      ).distinct()
      return post_list

# 정렬
class Mypage_CoverLetterSortList(MypageView):
   def get_queryset(self):
      q = self.kwargs['q']
      if q == "all":
         self.ordering = ['-pk']
      elif q == "latest":
         self.ordering = ['-create_at']
      elif q == "high":
         self.ordering = ['-rate']
      elif q == "low":
         self.ordering = ['rate']

      return super().get_queryset()


def findid(request):
   return render(request, "member/findid.html")

def findpw(request):
   return render(request, "member/findpassword.html")
