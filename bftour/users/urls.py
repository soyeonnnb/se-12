from django.urls import path

from . import views

app_name = "users"

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.Login.as_view(), name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.Register.as_view(), name="register"),
]
