from django.db import models
from member_site.models import User

# 이용 후기
class Review(models.Model):
   author = models.ForeignKey(User, on_delete=models.CASCADE)
   title = models.CharField(max_length=100)
   content = models.TextField()
   upload_file = models.FileField(upload_to="review/%Y/%m/%d/", null=True, blank=True)

   create_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)

# 이용 후기 댓글
class Reply(models.Model):
   author = models.ForeignKey(User, on_delete=models.CASCADE)
   review = models.ForeignKey(Review, on_delete=models.CASCADE)
   content = models.TextField()

   create_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)
