import datetime
from django.db.models.fields import related
from django.utils import timezone
from django.db import models
from django.conf import settings

from core import models as core_models


class BookedDay(core_models.TimeStampedModel):

    day = models.DateField()
    reservation = models.ForeignKey("Reservation", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Booked Day"
        verbose_name_plural = "Booked Days"

    def __str__(self):
        return str(self.day)


class Reservation(core_models.TimeStampedModel):

    """Reservation Model Definition"""

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

    STATUS_PENDING = "pending"
    STATUS_CONFIRMED = "confirmed"
    STATUS_CANCELED = "canceled"

    STATUS_CHOICES = (
        (STATUS_PENDING, "Pending"),
        (STATUS_CONFIRMED, "Confirmed"),
        (STATUS_CANCELED, "Canceled"),
    )

    status = models.CharField(
        max_length=12, choices=STATUS_CHOICES, default=STATUS_PENDING
    )

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

    payment = models.CharField(max_length=200, choices=PAYMENT_CHOICES)

    def __str__(self):
        return f"User:{self.user}-Hotel:{self.hotel}-Room:{self.room}-CheckInDate:{self.check_in}-CheckOutDate:{self.check_out}"

    def in_progress(self):
        now = timezone.now().date()
        return now >= self.check_in and now <= self.check_out

    in_progress.boolean = True

    def is_finished(self):
        now = timezone.now().date()
        is_finished = now > self.check_out
        if is_finished:
            BookedDay.objects.filter(reservation=self).delete()
        return is_finished

    is_finished.boolean = True

    def save(self, *args, **kwargs):
        if self.pk is None:
            start = self.check_in
            end = self.check_out
            difference = end - start
            existing_booked_day = BookedDay.objects.filter(
                day__range=(start, end)
            ).exists()
            if not existing_booked_day:
                super().save(*args, **kwargs)
                for i in range(difference.days + 1):
                    day = start + datetime.timedelta(days=i)
                    BookedDay.objects.create(day=day, reservation=self)
                return
        return super().save(*args, **kwargs)

    # 예약이 리뷰가 있는지 확인해주는 함수
    def has_reviews(self):
        all_reviews = self.reviews.all()
        return len(all_reviews) > 0
