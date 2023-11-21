from django.shortcuts import render, redirect
from django.views.generic import ListView

from .models import *
from .forms import *

# 메인
def index(request):
   return render(request, "coverletter_site/index.html")

# 회원가입
def join(request):
   # POST
   if request.method == "POST":
      form = UserForm(request.POST)
      if form.is_valid():
         form.save()
         print(form)
         return redirect('login')
   # GET
   form = UserForm()
   return render(request, "coverletter_site/join.html", {'userForm':form})

# 문서 업로드
def coverletter_upload(request):
   return render(request, "coverletter_site/coverletter_upload.html")

# 자소서 목록
class CoverLetterList(ListView):
   model = CoverLetter
   ordering = ['-pk']


def mypage(requset):
    return render(requset, "coverletter_site/mypage.html")


# 화면 확인용으로 임시로 만들었습니다. 편하신대로 바꾸시면 될 것 같습니다.
def review_list(requset):
    return render(requset, "coverletter_site/review_list.html")


def review_create(requset):
    return render(requset, "coverletter_site/review_create.html")


def check(requset):
    return render(requset, "coverletter_site/check.html")


def count(requset):
    return render(requset, "coverletter_site/count.html")