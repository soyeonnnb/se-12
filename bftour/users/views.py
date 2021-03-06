from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls.base import reverse_lazy
from django.views.generic import View, FormView, UpdateView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView

from . import forms
from . import models
from . import mixins


# login view
class Login(View):
    def get(self, request):
        form = forms.LoginForm()
        return render(request, "users/login.html", {"form": form})

    def post(self, request):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user_id = form.cleaned_data.get("user_id")
            password = form.cleaned_data.get("password")
            user = authenticate(request, user_id=user_id, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse("core:home"))
        return render(request, "users/login.html", {"form": form})


# Logout view
def logout_view(request):
    logout(request)
    return redirect(reverse_lazy("core:home"))


# 회원가입
class Register(FormView):

    template_name = "users/register.html"
    form_class = forms.RegisterForm
    success_url = reverse_lazy("core:home")

    def form_valid(self, form):
        form.save()
        user_id = form.cleaned_data.get("user_id")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, user_id=user_id, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)


# 사용자 정보
@login_required
def user_info_view(request):
    user = request.user
    user_info = models.User.objects.get(pk=user.pk)
    return render(request, "users/mypage.html", {"user_info": user_info})


# 사용자 정보 수정
class UpdateUser(mixins.LoggedInOnlyView, UpdateView):

    model = models.User
    form_class = forms.UserUpdateForm
    template_name = "users/user_update.html"
    success_url = reverse_lazy("users:mypage")

    def get_object(self, queryset=None):
        return self.request.user


# 회원 탈퇴
@login_required
def user_withdrawal(request):
    user = request.user
    user.delete()
    logout(request)
    return redirect(reverse_lazy("core:home"))


# 비밀번호 변경
class UpdatePasswordView(mixins.LoggedInOnlyView, PasswordChangeView):

    model = models.User
    template_name = "users/password_update.html"
    success_url = reverse_lazy("users:mypage")

    def get_object(self, queryset=None):
        return self.request.user
