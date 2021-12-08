from django.urls import path
from . import views

app_name = "reservations"

urlpatterns = [
   path("reservation_form/", views.CreateReservationView.as_view(), name='reservation_form'),
   # path("reservation_list/", views.ReservationListView.as_view(), name='reservation_list'),
   # path("reservation_detail/", views.ReservationDetailView.as_view(),name='reservation_detail'),
   # path("<int:pk>/create/", views.ReservationCreateView.as_view(), name='reservation_create'),
   path("<int:pk>/update/", views.UpdateReservationView.as_view(), name="update"),
   path("<int:pk>/delete/", views.DeleteReservationView.as_view(), name="delete"),
]