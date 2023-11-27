from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
# from hanspell import spell_checker
import json

# 메인
def index(request):
   return render(request, "web_site/index.html")

# 이용방법
def howtouse(request):
   return render(request, "web_site/howtouse.html")

def spelling_check_api(text_to_check):
    if text_to_check:  # 입력값이 있는지 확인
        # spelled_text = spell_checker.check(text_to_check)
        # checked_text = spelled_text.checked
        return {'corrected_text': checked_text}
    return {'error': 'Invalid input.'}

def spelling_check(request):
    if request.method == 'POST':
        text_to_check = request.POST.get('text')  # 사용자가 입력한 텍스트
        corrected_text = spelling_check_api(text_to_check)
        return JsonResponse(corrected_text)
    else:
        return render(request, "web_site/check.html")

def characters_count(request):
    return render(request, "web_site/count.html")
