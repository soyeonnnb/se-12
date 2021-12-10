from django.urls import path
from . import views

app_name = "rooms"

urlpatterns = [
    path("makeroom/<int:pk>", views.makeroom, name="makeroom"),
    path("deleteroom/<int:pk>/<int:fk>", views.deleteroom, name="deleteroom"),
    
    
]


