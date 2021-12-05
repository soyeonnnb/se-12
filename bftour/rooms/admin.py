from django.contrib import admin
from .import models
from .models import Room

# Register your models here.
admin.site.register(models.Room)