from django.db import models
from django.core.validators import MinValueValidator
from django.urls import reverse_lazy

# 상품 테이블
class Hotel(models.Model):

    mem_seq = models.ForeignKey("users.User", on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=False)
    contents = models.TextField(blank=False)
    address = models.CharField(max_length=255, blank=False)
    type = models.ManyToManyField("RoomType", related_name="hotels", blank=True)
    start_dt = models.DateTimeField("date published", blank=False)
    end_dt = models.DateTimeField("date published", blank=False)
    reg_dt = models.DateTimeField(auto_now_add=True)
    reg_id = models.CharField(max_length=50, default="admin")
    thumb_file = models.ImageField(
        null=True, blank=False, upload_to="hotel_thumb/%Y/%m/%d"
    )
    del_yn = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        url = reverse_lazy("detail", kwargs={"pk": self.pk})
        return url

    def get_rating(self):
        all_reviews = self.reviews.all()  # 해당 테이블을 fk로 가지는 reviews 테이블의 인스턴스를 가져옴
        all_ratings = 0
        if len(all_reviews) > 0:
            for review in all_reviews:
                all_ratings += (
                    review.rating
                )  # review테이블의 rating 애트리뷰트의 값 만큼 all_rating에 더해줌
            return round(all_ratings / len(all_reviews), 2)
        return 0


class RoomType(models.Model):

    name = models.CharField(max_length=60, default="")

    def __str__(self):
        return self.name
