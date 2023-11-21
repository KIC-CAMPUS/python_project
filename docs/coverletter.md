# CoverLetter 모델

#### `prj/coverletter_site/models.py`
```py
from django.db import models
from member_site.models import User

class CoverLetter(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
   document_type = models.CharField(max_length=100, choices=[('1', 'A'), ('2', 'B'), ('3', 'C'), ('4', 'D')])
   content = models.TextField(blank=True)
   document_file = models.FileField(upload_to="documents/%Y/%m/%d/", null=True)
   
   rate = models.DecimalField(max_digits=2, decimal_places=1, null=True)
   create_at = models.DateTimeField(auto_now_add=True)

   def __str__(self) -> str:
      return f'[{self.pk}] {self.document_type} :: {self.user}'
```
- `user`: 자소서를 업로드한 회원
- `document_type`: 문서의 유형
- `content`: 문서의 내용
- `document_file`: 업로드한 문서
- `rate`: 표절률
- `create_at`: 작성 날짜

## 연관관계
```
coverletter_site_coverletter -> member_site_user
```