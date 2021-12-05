from django.contrib import admin
from django.urls import path
from . import views
from .views import *

#이미지 URL 설정
from django.conf.urls.static import static
from django.conf import settings


app_name = "hotels"

urlpatterns = [
    path('index/', views.index, name='index'),
    path('blog/',blog, name='blog'),
    path('index/<int:pk>/',posting, name="posting"),
   
]

#이미지 url 설정
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
