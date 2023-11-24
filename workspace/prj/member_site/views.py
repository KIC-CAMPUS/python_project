from django.shortcuts import render
from django.contrib.auth import login
from .forms import UserForm
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from .forms import FindUsernameForm
from .forms import FindpwForm

from django.http import HttpResponse


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
def findid_(request):
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
def findpw_(request):
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



# 마이페이지
def mypage(request):
   return render(request, "member/mypage.html")

def findid(request):
   return render(request, "member/findid.html")

def findpassword(request):
   return render(request, "member/findpassword.html")



