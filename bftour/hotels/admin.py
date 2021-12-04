from django.contrib import admin

from .models import Post, tb_product
# Register your models here.

#Admin이 게시글에 접근 가능하게 함.
admin.site.register(Post)
admin.site.register(tb_product)
