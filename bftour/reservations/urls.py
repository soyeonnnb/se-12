from django.urls import path
from . import views

app_name = "reservations"

urlpatterns = [
    path("", views.view_reservations, name="reservation_list"),
    path(
        "<int:room_pk>/<check_in>/<check_out>/reservate/",
        views.CreateReservationView.as_view(),
        name="reservate",
    ),
    path("<int:pk>/update/", views.UpdateReservationView.as_view(), name="update"),
    path("<int:pk>/delete/", views.DeleteReservationView.as_view(), name="delete"),
]
