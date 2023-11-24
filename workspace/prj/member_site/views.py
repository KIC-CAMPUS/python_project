from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.urls import reverse_lazy

from .forms import UserForm
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

# 마이페이지
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