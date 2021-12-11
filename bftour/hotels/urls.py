from django.urls import path
from . import views


app_name = "hotels"

urlpatterns = [
    path("my_hotel/", views.my_hotel, name="my_hotel"),
    path(
        "my_hotel_reservation/<int:pk>",
        views.my_hotel_reservation,
        name="my_hotel_reservation",
    ),
    path("makehotel/", views.makehotels, name="makehotel"),
    path("<int:hotel_pk>/<check_in>/<check_out>/", views.viewhotel, name="viewhotel"),
    path("delete/<int:pk>", views.deletehotel, name="deletehotel"),
    path("update/<int:pk>", views.updatehotel, name="updatehotel"),
]
