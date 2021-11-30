from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls.base import reverse_lazy
from django.views.generic import View
from django.urls import reverse, reverse_lazy

from . import forms

# 아직 home이 없어서 user home을 만들어 주었음
def home(request):
    return render(request, "users/home.html")


# login view
class LoginView(View):
    def get(self, request):
        form = forms.LoginForm()
        return render(request, "users/login.html", {"form": form})

    def post(self, request):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            id = form.cleaned_data.get("id")
            password = form.cleaned_data.get("password")
            user = authenticate(request, user_id=id, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse("users:home"))
        return render(request, "users/login.html", {"form": form})


# Logout view
def logout_view(request):
    logout(request)
    return redirect(reverse_lazy("users:home"))

