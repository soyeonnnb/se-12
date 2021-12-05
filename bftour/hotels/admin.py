from django.contrib import admin

from .models import Post, tb_product
# Register your models here.

<<<<<<< HEAD
#Admin이 게시글에 접근 가능하게 함.
admin.site.register(Post)
admin.site.register(tb_product)
=======
admin.site.register(models.Hotel)
admin.site.register(models.RoomType)
>>>>>>> c5d96df0ffcef99a0a37c7a9116c9581c6829eaf
