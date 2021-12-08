from django.db import models

# Create your models here.
class Room(models.Model):

    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="rooms"
    )
    hotel = models.ForeignKey(
        "hotels.Hotel", on_delete=models.CASCADE, related_name="rooms"
    )
    
    room_name = models.CharField(max_length=50, default="")
    price = models.CharField(max_length=50, default="") 
    
    def __str__(self):
        return self.room_name

