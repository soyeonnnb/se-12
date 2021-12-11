from django.db import models
from django.core.validators import MinValueValidator
from django.urls import reverse_lazy

# 상품 테이블
class Hotel(models.Model):

    mem_seq = models.ForeignKey("users.User", on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    contents = models.TextField()
    address = models.CharField(max_length=255)
    type = models.ManyToManyField("RoomType", related_name="hotels", blank=True)
    start_dt = models.DateTimeField("date published")
    end_dt = models.DateTimeField("date published")
    reg_dt = models.DateTimeField(auto_now_add=True)
    reg_id = models.CharField(max_length=50, default="admin")
    thumb_file = models.ImageField(
        null=True, blank=True, upload_to="hotel_thumb/%Y/%m/%d"
    )
    del_yn = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        url = reverse_lazy("detail", kwargs={"pk": self.pk})
        return url


class RoomType(models.Model):

    name = models.CharField(max_length=60, default="")

    def __str__(self):
        return self.name
