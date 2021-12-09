import datetime
from django.db.models.fields import related
from django.utils import timezone
from django.db import models
from django.conf import settings

from core import models as core_models

class Reservation(core_models.TimeStampedModel):

    """Reservation Model Definition"""
    check_in = models.DateField()
    check_out = models.DateField()
    
    request = models.TextField()
    
    user = models.ForeignKey(
        "users.User", related_name="reservations", on_delete=models.CASCADE
    )
    
    room = models.ForeignKey(
        "rooms.Room", related_name="reservations", on_delete=models.CASCADE
    )
    
    hotel = models.ForeignKey(
        "hotels.Hotel", related_name="reservations", on_delete=models.CASCADE
    )
    
    PAYMENT_CREDITCARD = "credit_card"
    PAYMENT_VIRTUALACCOUNT = "virtual_account"
    PAYMENT_TRANSFERACCOUNT = "transfer_account"
    PAYMENT_PHONE = "phone"
    PAYMENT_TOSS = "toss"
    PAYMENT_KAKAOPAY = "kakaopay"
    PAYMENT_NAVERPAY = "naverpay"
    PAYMENT_PAYCO = "payco"

    PAYMENT_CHOICES = (
        (PAYMENT_CREDITCARD, "Credit card"),
        (PAYMENT_VIRTUALACCOUNT, "Virtual account"),
        (PAYMENT_TRANSFERACCOUNT, "Transfer account"),
        (PAYMENT_PHONE, "Phone"),
        (PAYMENT_TOSS, "TOSS"),
        (PAYMENT_KAKAOPAY, "KAKAOPAY"),
        (PAYMENT_NAVERPAY, "NAVERPAY"),
        (PAYMENT_PAYCO, "PAYCO"),
    )

    payment = models.CharField(
       max_length=200, choices=PAYMENT_CHOICES
    )

    def __str__(self):
        return f"User:{self.user}-Hotel:{self.hotel}-Room:{self.room}-CheckInDate:{self.check_in}-CheckOutDate:{self.check_out}"

    # 예약이 리뷰가 있는지 확인해주는 함수
    def has_reviews(self):
        all_reviews = self.reviews.all()
        return len(all_reviews) > 0