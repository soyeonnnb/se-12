from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.


class Post(models.Model):
    postname = models.CharField(max_length=50)

    contents = models.TextField()

    def __str__(self):
        return self.postname


# 상품 테이블
class Hotel(models.Model):

    mem_seq = models.ForeignKey("users.User", on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    contents = models.TextField()
    place = models.TextField()
    address = models.CharField(max_length=255)
    # type = 체크박스
    type = models.ManyToManyField(
        "RoomType", related_name="hotels", null=True, blank=True
    )
    start_dt = models.DateTimeField("date published")
    end_dt = models.DateTimeField("date published")
    pro_price = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    reg_dt = models.DateTimeField(auto_now_add=True)
    reg_id = models.CharField(max_length=50, default="admin")
    thumb_file = models.ImageField(
        null=True, blank=True, upload_to="hotel_thumb/%Y/%m/%d"
    )
    # reserve_yn = models.CharField(max_length = 1, default='N')
    del_yn = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class RoomType(models.Model):

    name = models.CharField(max_length=60, default="")
    
    def __str__(self):
        return self.name