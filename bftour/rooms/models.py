from django.db import models

# Create your models here.
class Room(models.Model):

    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="rooms"
    )
    hotel = models.ForeignKey(
        "hotels.Hotel", on_delete=models.CASCADE, related_name="rooms"
    )
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.hotel} - {self.name}"
