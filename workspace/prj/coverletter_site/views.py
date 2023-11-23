from typing import Any
from django.db.models.query import QuerySet
from django.db.models import Q
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import CoverLetter
from .forms import CoverLetterForm
from .plagiarism_check_model import document_rate_check

# 문서 업로드
class CoverLetterCreated(LoginRequiredMixin, CreateView):
   model = CoverLetter
   form_class = CoverLetterForm
   success_url = reverse_lazy('result_list')
   login_url = reverse_lazy('login')

   def form_valid(self, form: BaseModelForm) -> HttpResponse:
      coverletter = form.save(commit=False)
      coverletter.user = self.request.user
      reps = super().form_valid(form)
      if coverletter.document_file != None:
         docs_path = r'%s' % coverletter.document_file.name
         document_rate_check(docs_path)
      return reps



# 자소서 목록
class CoverLetterList(LoginRequiredMixin, ListView):
   model = CoverLetter
   ordering = ['-pk']
   paginate_by = 5
   login_url = reverse_lazy('login')

   def get_queryset(self) -> QuerySet[Any]:
      user = self.request.user
      return super().get_queryset().filter(user=user)

# 자소서 표절 결과 상세 페이지
class CoverLetterDetail(DetailView):
   model = CoverLetter

# 자소서 표절 결과 목록
# class CoverLetterResultList(CoverLetterList):
#    template_name = "coverletter_site/detail.html"

#    def get_queryset(self) -> QuerySet[Any]:
#       user = self.request.user
#       return super(ListView, self).get_queryset().filter(~Q(rate__exact=None), user=user)

# 문서 삭제
def CoverLetterDelete(request):
   if request.method == 'POST':
      pk_list = request.POST.getlist('chk')
      CoverLetter.objects.filter(pk__in=pk_list).delete()
   return redirect(reverse_lazy('result_list'))


# def post_like(request):
#    if request.method == 'POST':
#       pk = request.POST.get('pk', None)  # ajax 통신을 통해서 template에서 POST방식으로 전달
#       post = get_object_or_404(Post, pk=pk)
#       post_like, post_like_created = post.like_set.get_or_create(user=request.user)
#
#       if not post_like_created:
#          post_like.delete()
#
#       return HttpResponse(content_type="application/json")

class PostSearch(CoverLetterList):
   def get_queryset(self):
      q = self.kwargs['q']
      post_list = super().get_queryset().filter(
         Q(title__contains=q)
      ).distinct()
      return post_list
