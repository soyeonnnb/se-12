from django.contrib import admin
from .import models
from .models import  Hotel
# Register your models here.

admin.site.register(models.Hotel)
admin.site.register(models.RoomType)