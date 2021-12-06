from django.contrib import admin 
from django.urls import path

from . import views

app_name = "payments"

urlpatterns = [
    path('', views.index, name='index')
    # path("paymentdetail", views.payment_detail_view, name="paymentdetail"),
]
