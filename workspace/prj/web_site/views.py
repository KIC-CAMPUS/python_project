from django.shortcuts import render

# 메인
def index(request):
   return render(request, "web_site/index.html")

# 이용방법
def howtouse(request):
   return render(request, "web_site/howtouse.html")

def spelling_check(requset):
   return render(requset, "web_site/check.html")

def characters_count(requset):
   return render(requset, "web_site/count.html")