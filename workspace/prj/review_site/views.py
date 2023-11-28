from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404, redirect

from .models import Review, Comment

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

# 이용 후기 수정
class ReviewUpdateView(UpdateView):
   model = Review
   fields = ('title', 'content', 'upload_file')
   template_name = 'review_site/review_edit.html'

# 댓글 등록
def add_comment(request, pk):
   review = get_object_or_404(Review, pk=pk)
   if request.method == 'POST':
      content = request.POST.get('comment')
      author = request.user if request.user.is_authenticated else None
      if author:
         Comment.objects.create(review=review, content=content, author=author)
      else:
         return redirect(reverse('login'))
   return redirect('review_detail', pk=pk)

# 댓글 삭제
def delete_comment(request, comment_id):
   comment = get_object_or_404(Comment, pk=comment_id)
   if request.user == comment.author:
      comment.delete()
      return redirect('review_detail', pk=comment.review.pk)
   else:
      return HttpResponse("삭제 권한이 없습니다.")