# config.urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('web_site.urls')),
    path('coverletter/', include('coverletter_site.urls')),
    path('', include('member_site.urls')),
    path('review/', include('review_site.urls')),
]