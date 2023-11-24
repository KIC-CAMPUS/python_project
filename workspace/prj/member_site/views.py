from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.http import HttpResponse

from .forms import UserForm
from .forms import FindUsernameForm
from .forms import FindpwForm
from coverletter_site.models import CoverLetter
from coverletter_site.views import CoverLetterList, coverLetterDelete


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
def findid(request):
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
            username = "일치하는 사용자가 없어요."

   return render(request, "member/id_success.html", {'form': form, 'username': username})

#비밀번호 찾기
def findpw(request):
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
            password1 = user.password
         except ObjectDoesNotExist as e:
            print(f"ObjectDoesNotExist exception: {e}")
            password1 = "일치하는 사용자가 없어요."

   return render(request, "member/pw_success.html", {'form': form, 'password1': password1})

class MypageView(CoverLetterList):
   template_name = "member/mypage.html"

# 페이지 볼려고 추가했습니다. 무시하셔도 될거 같아요
# 마이페이지 수정
def mypage_edit(request):
   return render(request, "member/mypage_edit.html")

def mypage_coverLetterDelete(request):
   coverLetterDelete(request)
   return redirect(reverse_lazy('mypage'))

def post_like(request):
   if request.method == 'POST':
      pk = request.POST.get('pk', None)  # ajax 통신을 통해서 template에서 POST방식으로 전달
      post = get_object_or_404(CoverLetter, pk=pk)
      post_like, post_like_created = post.like_set.get_or_create(user=request.user)

      if not post_like_created:
         post_like.delete()

      return HttpResponse(content_type="application/json")

class PostSearch(MypageView):
   def get_queryset(self):
      q = self.kwargs['q']
      post_list = super().get_queryset().filter(
         Q(title__contains=q)
      ).distinct()
      return post_list

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

