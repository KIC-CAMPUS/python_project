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
    if request.method == 'POST':
        return handle_characters_count(request)
    else:
        return render(request, "web_site/count.html")


def handle_characters_count(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        text_to_count = data.get('text', '')

        total_characters = len(text_to_count)
        total_bytes = len(text_to_count.encode('utf-8'))

        text_without_spaces = text_to_count.replace(' ', '')  # 공백 제외한 텍스트

        total_characters_without_spaces = len(text_without_spaces)
        total_bytes_without_spaces = len(text_without_spaces.encode('utf-8'))

        response_data = {
            'total_characters': total_characters,
            'total_bytes': total_bytes,
            'total_characters_without_spaces': total_characters_without_spaces,
            'total_bytes_without_spaces': total_bytes_without_spaces,
        }

        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Invalid request'})
