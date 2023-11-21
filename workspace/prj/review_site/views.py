from typing import Any
from django.shortcuts import render
from django.db.models.query import QuerySet
from django.views.generic import ListView, CreateView
from django.urls import reverse, reverse_lazy

from .models import Review, Reply

# 이용 후기 작성
class ReviewCreated(CreateView):
   model = Review
   fields = ('title', 'content', 'upload_file')
   success_url = reverse_lazy('review_list')

   def get_success_url(self) -> str:
      obj = self.object
      obj.user = self.request.user
      obj.save()
      return reverse('review_list')

# 이용 후기 목록
class ReviewList(ListView):
   model = Review
   ordering = ['-pk']
   paginate_by = 5