# config.urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('coverletter_site.urls')),
    path('', include('member_site.urls')),
    path('', include('review_site.urls')),
]