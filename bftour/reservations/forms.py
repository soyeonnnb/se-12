from django import forms
from . import models

class ReservationList(forms.ModelForm):
    class Meta:
        model = models.Reservation
        fields = "__all__"
    def __init__(self, *args, **kwargs):
        super(ReservationList, self).__init__(*args, **kwargs)
    

class ReservationForm(forms.ModelForm):
    class Meta:
        model = models.Reservation
        fields = ("hotel", "room", "check_in", "check_out")
        
    def __init__(self, *args, **kwargs):
        super(ReservationForm, self).__init__(*args, **kwargs)