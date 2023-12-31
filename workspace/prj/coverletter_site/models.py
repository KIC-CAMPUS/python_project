from django.db import models
from member_site.models import User

# 자소서 문서 유형
document_type_list = [
   (1, '입사 포부'), (2, '지원 동기'), (3, '성격'), 
   (4, '팀워크'), (5, '기타'), 
]

# 자소서
class CoverLetter(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   document_type = models.IntegerField(choices=document_type_list)
   title = models.CharField(max_length=100)
   content = models.TextField()
   
   rate = models.DecimalField(max_digits=5, decimal_places=3, null=True)
   create_at = models.DateTimeField(auto_now_add=True)

   bookmark = models.BooleanField(default=False)

   def __str__(self) -> str:
      return f'[{self.pk}] {self.title} :: {self.user}'
   
   def get_rate_per(self):
      return '%2.2f'% (self.rate * 100)

   def get_rate_per_not(self):
      return '%2.2f' % (100 - self.rate * 100)
   
   def get_document_type_str(self):
      return document_type_list[self.document_type - 1][1]

class CoverLetterPlagiarism(models.Model):
   coverletter = models.ForeignKey(CoverLetter, on_delete=models.CASCADE)
   query_sentence = models.TextField()
   most_similar = models.TextField()
   result = models.DecimalField(max_digits=6, decimal_places=3, null=True)
   sequence_number = models.IntegerField()

   def __str__(self) -> str:
      return f'[{self.pk}] {self.coverletter} {self.query_sentence} :: {self.result}'
   
   def get_result_per(self):
      return '%2.2f'% (self.result * 100)