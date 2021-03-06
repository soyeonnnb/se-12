from django.contrib import admin
from . import models


@admin.register(models.Reservation)
class ReservationAdmin(admin.ModelAdmin):

    """Reservation Admin Definition"""

    list_display = (
        "hotel",
        "room",
        "status",
        "check_in",
        "check_out",
        "user",
        "in_progress",
        "is_finished",
    )

    list_filter = ("status",)


@admin.register(models.BookedDay)
class ReservationBookeddayAdmin(admin.ModelAdmin):

    list_display = ("reservation", "day")
