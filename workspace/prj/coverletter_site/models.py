from django.db import models
from member_site.models import User

# 자소서 문서 유형
document_type_list = [
   ('1', '성장 과정'), ('2', '장점과 단점'), ('3', '지원 동기'), ('4', '입사 후 포부'), ('5', '기타'),
]

# 자소서
class CoverLetter(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
   document_type = models.CharField(max_length=100, choices=document_type_list)
   title = models.CharField(max_length=100, blank=True)
   content = models.TextField(blank=True)
   
   rate = models.DecimalField(max_digits=3, decimal_places=3, null=True)
   create_at = models.DateTimeField(auto_now_add=True)

   bookmark = models.BooleanField(default=False)

   def __str__(self) -> str:
      return f'[{self.pk}] {self.document_type} :: {self.user}'
   
   def get_rate_per(self):
      return '%2.2f'% (self.rate * 100)
