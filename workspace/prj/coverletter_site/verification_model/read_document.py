from docx import Document
from django.conf import settings
import os

def document_rate_check(docx_path):
   docx_path = os.path.join(settings.MEDIA_ROOT, docx_path)
   doc = Document(docx_path)