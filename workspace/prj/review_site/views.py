from django.shortcuts import render

def review_list(requset):
   return render(requset, "review/review_list.html")

def review_create(requset):
   return render(requset, "review/review_create.html")