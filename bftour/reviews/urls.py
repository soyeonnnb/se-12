from django.urls import path

from . import views

app_name = "reviews"

urlpatterns = [
    path("reservation", views.view_reservation, name="reservation"),
    path("<int:pk>/create/", views.make_review, name="create"),
]
