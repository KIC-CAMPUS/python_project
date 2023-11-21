from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from django.urls import reverse_lazy

from .models import Review, Reply

# 이용 후기 작성
class ReviewCreated(CreateView):
   model = Review
   fields = ('title', 'content', 'upload_file')
   success_url = reverse_lazy('review_list')

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

# 댓글 작성
class ReplyCreated(CreateView):
   model = Reply
   fields = ('content')

   def form_valid(self, form: BaseModelForm) -> HttpResponse:
      review = form.save(commit=False)
      review.author = self.request.user
      return super(ReplyCreated, self).form_valid(form)