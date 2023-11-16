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