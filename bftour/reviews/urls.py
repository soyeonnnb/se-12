from django.urls import path

from . import views

app_name = "reviews"

urlpatterns = [
    path("reservation", views.view_reservations, name="reservation"),
    path("my_reviews/", views.view_reviews, name="view"),
    path("<int:pk>/create/", views.make_review, name="create"),
    path("<int:pk>/update/", views.UpdateReview.as_view(), name="update"),
    path("<int:pk>/delete/", views.DeleteReview.as_view(), name="delete"),
]
