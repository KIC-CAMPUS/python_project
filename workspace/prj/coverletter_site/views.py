from typing import Any
from django.db.models.query import QuerySet
from django.db.models import Q
from django.forms.models import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import CoverLetter, CoverLetterPlagiarism
from .forms import CoverLetterForm
from .verification_model.plagiarism_rate import sentence_plagiarism_rate

# 문서 업로드
class CoverLetterCreated(LoginRequiredMixin, CreateView):
   model = CoverLetter
   form_class = CoverLetterForm
   success_url = reverse_lazy('result_list')
   login_url = reverse_lazy('login')

   def form_valid(self, form: BaseModelForm) -> HttpResponse:
      coverletter = form.save(commit=False)
      coverletter.user = self.request.user
      rate, list_query_sentence = sentence_plagiarism_rate(coverletter.content, coverletter.document_type)
      coverletter.rate = float(rate)
      print(list_query_sentence)
      resp = super().form_valid(form)
      for query in list_query_sentence:
         cl_plagiarism = CoverLetterPlagiarism(coverletter = coverletter)
         cl_plagiarism.query_sentence = query['query_sentence']
         cl_plagiarism.most_similar = query['most_similar']
         cl_plagiarism.result = float(query['result'])
         cl_plagiarism.sequence_number = query['sequence_number']
         cl_plagiarism.save()
      return resp
   
   def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
      super().post(request, *args, **kwargs)
      return HttpResponse(self.success_url)

# 자소서 목록
class CoverLetterList(LoginRequiredMixin, ListView):
   model = CoverLetter
   ordering = ['-pk']
   paginate_by = 5
   login_url = reverse_lazy('login')

   def get_queryset(self) -> QuerySet[Any]:
      user = self.request.user
      qs = super().get_queryset().filter(user=user)
      
      self.search = self.request.GET.get('search', '').strip()
      qs = qs.filter(Q(title__contains=self.search))
      return qs
   
   def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
      context = super().get_context_data(**kwargs)
      context['query_string'] = ''
      if self.search:
         context['query_string'] += '&search=' + self.search
      print(context['query_string'])
      return context

class CoverLetterSortList(CoverLetterList):
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

# 자소서 표절 결과 상세 페이지
class CoverLetterDetail(DetailView):
   model = CoverLetter

   def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
      context = super().get_context_data(**kwargs)
      plagiarism_list = CoverLetterPlagiarism.objects.filter(coverletter=self.object).order_by('sequence_number')
      
      max_reulst = max(map(lambda x: x.result, plagiarism_list))
      plagiarism_sentence = list(filter(lambda x: x.result > 0.4, plagiarism_list))
      
      context['max_reulst'] = '%.2f' % (max_reulst * 100)
      context['plagiarism_sentence_count'] = len(plagiarism_sentence)
      context['plagiarism_list'] = plagiarism_list
      return context

# 문서 삭제
def coverLetterDelete(request):
   if request.method == 'POST':
      pk_list = request.POST.getlist('chk')
      CoverLetter.objects.filter(pk__in=pk_list).delete()
   return redirect(reverse_lazy('result_list'))

def coverletter_bookmark(request):
   if request.method == 'POST':
      pk = request.POST.get('pk', None)  # ajax 통신을 통해서 template에서 POST방식으로 전달
      post = get_object_or_404(CoverLetter, pk=pk)
      post.bookmark = not post.bookmark
      post.save()
      return HttpResponse()