from typing import Any
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Review, Reply

# 이용 후기 작성
class ReviewCreated(LoginRequiredMixin, CreateView):
   model = Review
   fields = ('title', 'content', 'upload_file')
   login_url = reverse_lazy('login')

   def form_valid(self, form: BaseModelForm) -> HttpResponse:
      review = form.save(commit=False)
      review.author = self.request.user
      return super(ReviewCreated, self).form_valid(form)

# 이용 후기 목록
class ReviewList(ListView):
   model = Review
   ordering = ['-pk']
   paginate_by = 5

# 이용 후기 조회
class ReviewDetail(DetailView):
   model = Review

   # 댓글 목록 임시로 만듦..
   def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
      context = super().get_context_data(**kwargs)
      context['reply_list'] = Reply.objects.filter(review = self.get_object()).all()
      return context
   
class ReviewEdit(UpdateView):
   model = Review
   fields = ('title', 'content', 'upload_file')