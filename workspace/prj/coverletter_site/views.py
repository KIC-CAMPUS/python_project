from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView

from .models import CoverLetter
from .forms import CoverLetterForm

# 메인
def index(request):
   return render(request, "coverletter_site/index.html")

# 마이페이지
def mypage(request):
   return render(request, "coverletter_site/mypage.html")

# 이용방법
def howtouse(request):
   return render(request, "coverletter_site/howtouse.html")

def spelling_check(requset):
   return render(requset, "coverletter_site/check.html")

def characters_count(requset):
   return render(requset, "coverletter_site/count.html")

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
