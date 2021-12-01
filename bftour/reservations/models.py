from django.db import models

# Create your models here.
class Reservation(models.Model):

    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="reservations"
    )
    room = models.ForeignKey(
        "rooms.Room", on_delete=models.CASCADE, related_name="reservations"
    )

    # 예약이 리뷰가 있는지 확인해주는 함수
    def has_reviews(self):
        all_reviews = self.reviews.all()
        return len(all_reviews) > 0
