from django.db import models

# Create your models here.
class Room(models.Model):

    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="rooms"
    )
    hotel = models.ForeignKey(
        "hotels.Hotel", on_delete=models.CASCADE, related_name="rooms"
    )
