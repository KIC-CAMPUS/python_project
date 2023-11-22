from django.shortcuts import render
from django.contrib.auth import login
from .forms import UserForm

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

# 마이페이지
def mypage(request):
   return render(request, "member/mypage.html")