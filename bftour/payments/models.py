from django.db import models
from django import forms

# Create your models here.
class Payment(models.Model):

    PAYMENT_CREDITCARD = "credit card"
    PAYMENT_VIRTUALACCOUNT = "virtual account"
    PAYMENT_TRANSFERACCOUNT = "transfer account"
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
    
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="payments"
    )
    room = models.ForeignKey(
        "rooms.Room", on_delete=models.CASCADE, related_name="payments"
    )
    hotel = models.ForeignKey(
        "hotels.Hotel", on_delete=models.CASCADE, related_name="payments"
    )
    
    def __str__(self):
        return self.name

    
    