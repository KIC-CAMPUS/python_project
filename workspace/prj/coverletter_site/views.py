from django.shortcuts import render
from django.views.generic import ListView

from .models import *
from .forms import *

def index(request):
   return render(request, "coverletter_site/index.html")

def login(request):
   return render(request, "coverletter_site/login.html")

def coverletter_upload(request):
   return render(request, "coverletter_site/coverletter_upload.html")

# 자소서 목록
class CoverLetterList(ListView):
   model = CoverLetter
   ordering = ['-pk']