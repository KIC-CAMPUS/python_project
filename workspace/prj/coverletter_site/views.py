from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView
from django.contrib.auth import login

from .models import User, CoverLetter
from .forms import UserForm, CoverLetterForm

# 메인
def index(request):
   return render(request, "coverletter_site/index.html")

# 마이페이지
def mypage(request):
   return render(request, "coverletter_site/mypage.html")

# 이용방법
def howtouse(request):
   return render(request, "coverletter_site/howtouse.html")

# 회원가입
def join(request):
   # POST
   if request.method == "POST":
      form = UserForm(request.POST)
      if form.is_valid():
         join_user = form.save()
         login(request, join_user)
         return render(request, "coverletter_site/join_success.html")
   # GET
   else :
      form = UserForm()
   return render(request, "coverletter_site/join.html", {'form': form})

# 문서 업로드
class CoverLetterCreated(CreateView):
   model = CoverLetter
   form_class = CoverLetterForm
   success_url = reverse_lazy('result_list')

   def get_success_url(self) -> str:
      obj = self.object
      obj.user = self.request.user
      obj.save()
      return reverse('result_list')

# 자소서 목록
class CoverLetterList(ListView):
   model = CoverLetter
   ordering = ['-pk']
   paginate_by = 5

   def get_queryset(self) -> QuerySet[Any]:
      user = self.request.user
      return super().get_queryset().filter(user=user)