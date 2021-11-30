from django.urls import path

from . import views

app_name = "users"

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.Login.as_view(), name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("mypage/", views.user_info_view, name="mypage"),
    path("update/", views.UpdateUser.as_view(), name="update"),
    path("register/", views.Register.as_view(), name="register"),
    path("delete/", views.Register.as_view(), name="delete"),
]
