from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import check_password

from . import models


# 로그인 Form
class LoginForm(forms.Form):

    user_id = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        user_id = self.cleaned_data.get("user_id")
        password = self.cleaned_data.get("password")
        try:
            user = models.User.objects.get(user_id=user_id)
            if user.check_password(password):
                return self.cleaned_data
            else:
                self.add_error("password", forms.ValidationError("비밀번호가 틀렸습니다."))
        except:
            self.add_error("user_id", forms.ValidationError("아이디가 존재하지 않습니다."))


# 회원가입 Form 
class RegisterForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ("is_host", "user_id", "name", "phone", "email")

    password = forms.CharField(widget=forms.PasswordInput(attrs={"label": "비밀번호"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"label": "비밀번호 확인"}))

    def clean_user_id(self):
        user_id = self.cleaned_data.get("user_id")
        try:
            models.User.objects.get(user_id=user_id)
            self.add_error("user_id", ValidationError("이미 존재하는 아이디입니다."))
        except models.User.DoesNotExist:
            return user_id

    def clean_email(self):
        email = self.cleaned_data.get("email")
        try:
            models.User.objects.get(email=email)
            self.add_error("email", ValidationError("이미 존재하는 이메일입니다."))
        except models.User.DoesNotExist:
            return email

    def clean_password1(self):
        password = self.cleaned_data.get("password")
        password1 = self.cleaned_data.get("password1")
        if password != password1:
            self.add_error("password1", ValidationError("비밀번호가 일치하지 않습니다."))
        else:
            return password1

    def save(self, *args, **kwargs):
        user = super().save(commit=False)
        user_id = self.cleaned_data.get("user_id")
        password = self.cleaned_data.get("password")
        user.username = user_id
        user.set_password(password)
        user.save()


# 회원정보 수정 Form
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = (
            "name",
            "phone",
            "email", 
        )
