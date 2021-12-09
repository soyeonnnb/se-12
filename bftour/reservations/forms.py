from django import forms
from . import models


class ReservationForm(forms.ModelForm):
    class Meta:
        model = models.Reservation
        fields = ("request", "payment", "check_in", "check_out")

    def __init__(self, *args, **kwargs):
        super(ReservationForm, self).__init__(*args, **kwargs)
