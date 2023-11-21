from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, CreateView
from django.contrib.auth import login

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

# 자소서 목록
class CoverLetterList(ListView):
   model = CoverLetter
   ordering = ['-pk']
   paginate_by = 5

class Howtouse(View):
   template_name = 'howtouse.html'
   def get(self, request, *args, **kwargs):
      return render(request, 'coverletter_site/howtouse.html')