from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import check_password

from .models import Payment

# 예약자 정보 Form


# 결제 수단 Form
class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['payment'].queryset = Payment.objects.none()
        
