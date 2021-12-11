from django.urls import path
from . import views


app_name = "hotels"

urlpatterns = [
    path("index/", views.index, name="index"),
    path("makehotel/", views.makehotels, name="makehotel"),
    path("<int:hotel_pk>/<check_in>/<check_out>/", views.viewhotel, name="viewhotel"),
    path("delete/<int:pk>", views.deletehotel, name="deletehotel"),
    path("update/<int:pk>", views.updatehotel, name="updatehotel"),
]
