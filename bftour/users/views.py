from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls.base import reverse_lazy
from django.views.generic import View, FormView
from django.urls import reverse, reverse_lazy

from . import forms

# 아직 home이 없어서 user home을 만들어 주었음
def home(request):
    return render(request, "users/home.html")


# login view
class Login(View):
    def get(self, request):
        form = forms.LoginForm()
        return render(request, "users/login.html", {"form": form})

    def post(self, request):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user_id = form.cleaned_data.get("id")
            password = form.cleaned_data.get("password")
            user = authenticate(request, user_id=user_id, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse("users:home"))
        return render(request, "users/login.html", {"form": form})


# Logout view
def logout_view(request):
    logout(request)
    return redirect(reverse_lazy("users:home"))


# 회원가입
class Register(FormView):

    template_name = "users/register.html"
    form_class = forms.RegisterForm
    success_url = reverse_lazy("users:home")

    def form_valid(self, form):
        form.save()
        user_id = form.cleaned_data.get("user_id")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, user_id=user_id, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)
