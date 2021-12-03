from django.contrib import admin
from django.urls import path
from . import views
from .views import *


app_name = "hotels"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('blog/',blog, name='blog'),
    path('blog/<int:pk>/',posting, name="posting"),
   
]

