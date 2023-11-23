from .models import  CoverLetter
from django import forms

class CoverLetterForm(forms.ModelForm):
   document_file = forms.FileField(required=False, label='검사 문서')

   class Meta:
      model = CoverLetter
      fields = ("document_type", "title","content", "document_file")

      widgets = {
         'document_type': forms.Select(attrs={'class': 'custom-select'}),
         'title': forms.TextInput(attrs={'class': 'form-control'}),
         'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
         'document_file': forms.FileInput(attrs={'class': 'form-control'}),
      }

      labels = {
         'document_type': '문서 유형',
         'title': '제목',
         'content': '내용',
      }  