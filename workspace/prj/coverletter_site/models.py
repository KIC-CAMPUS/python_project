from django.db import models
from member_site.models import User

# 자소서 문서 유형
document_type_list = [
   ('1', '성장 과정'), ('2', '장점과 단점'), ('3', '지원 동기'), ('4', '입사 후 포부'),
]

# 자소서
class CoverLetter(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
   document_type = models.CharField(max_length=100, choices=document_type_list)
   title = models.CharField(max_length=100, blank=True)
   content = models.TextField(blank=True)
   document_file = models.FileField(upload_to="documents/%Y/%m/%d/", null=True)
   
   rate = models.DecimalField(max_digits=2, decimal_places=1, null=True)
   create_at = models.DateTimeField(auto_now_add=True)

   like_user_set = models.ManyToManyField(User, blank=True, related_name='like_user_set', through='Like')

   def __str__(self) -> str:
      return f'[{self.pk}] {self.document_type} :: {self.user}'

# 즐겨찾기
class Like(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   post = models.ForeignKey(CoverLetter, on_delete=models.CASCADE)
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)

   # 한번만 누를수 있음
   class Meta:
      unique_together = (
         ('user', 'post')
      )
      
