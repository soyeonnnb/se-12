from django.db import models

# Create your models here.
class Reservation(models.Model):

    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="reservations"
    )
    room = models.ForeignKey(
        "rooms.Room", on_delete=models.CASCADE, related_name="reservations"
    )
