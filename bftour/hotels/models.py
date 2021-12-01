from django.db import models

# Create your models here.
class Hotel(models.Model):

    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="hotels"
    )
    name = models.CharField(max_length=50)
