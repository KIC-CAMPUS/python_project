from .models import  CoverLetter
from django import forms

class CoverLetterForm(forms.ModelForm):
   document_file = forms.FileField(required=False)
   class Meta:
      model = CoverLetter
      fields = ("document_type", "content", "document_file")