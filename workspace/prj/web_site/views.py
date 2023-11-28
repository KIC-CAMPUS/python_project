from django.shortcuts import render

# 메인
def index(request):
    return render(request, "web_site/index.html")

# 이용방법
def howtouse(request):
    return render(request, "web_site/howtouse.html")

def characters_count(request):
    return render(request, "web_site/count.html")
