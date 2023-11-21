# Review 모델

#### `prj/review_site/models.py`
```py
from django.db import models
from member_site.models import User

class Review(models.Model):
   author = models.ForeignKey(User, on_delete=models.CASCADE)
   title = models.CharField(max_length=100)
   content = models.TextField()

   create_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)
```
- `author`: 후기를 작성한 회원
- `title`: 제목
- `content`: 내용
- `create_at`: 작성한 날짜
- `updated_at`: 수정한 날짜

# Reply 모델

#### `prj/review_site/models.py`
```py
from django.db import models
from member_site.models import User

class Reply(models.Model):
   author = models.ForeignKey(User, on_delete=models.CASCADE)
   review = models.ForeignKey(Review, on_delete=models.CASCADE)
   content = models.TextField()

   create_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)
```
- `author`: 댓글을 작성한 회원
- `review`: 댓글을 단 후기글
- `content`: 내용
- `create_at`: 작성한 날짜
- `updated_at`: 수정한 날짜

## 연관관계
```
      ┌─> member_site_user <─┐
review_site_review <- review_site_reply
```