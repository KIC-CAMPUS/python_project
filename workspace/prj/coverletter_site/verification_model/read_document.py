from docx import Document
from django.conf import settings
import os

def document_rate_check(docx_path):
   docx_path = os.path.join(settings.MEDIA_ROOT, docx_path)
   print('문서 읽기: ',docx_path)
   doc = Document(docx_path)
   for i, paragraph in enumerate(doc.paragraphs):
      print(str(i+1) + ": " + paragraph.text)