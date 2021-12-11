from django import forms
from rooms.models import Room


class MakeRoom(forms.ModelForm):
    class Meta:

        model = Room
        fields = ["room_name", "price"]
        labels = {"room_name": "객실 이름", "price": "객실 가격"}
