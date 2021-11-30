from django import forms

from . import models


class LoginForm(forms.Form):
    id = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        id = self.cleaned_data.get("id")
        password = self.cleaned_data.get("password")
        try:
            user = models.User.objects.get(user_id=id)
            if user.check_password(password):
                return self.cleaned_data
            else:
                self.add_error("password", forms.ValidationError("비밀번호가 틀렸습니다."))
        except:
            self.add_error("id", forms.ValidationError("아이디가 존재하지 않습니다."))
