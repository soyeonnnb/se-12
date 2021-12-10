from django import forms
from .models import Hotel, RoomType
from rooms.models import Room


class MakeHotel(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = [
            "title",
            "contents",
            "type",
            "address",
            "start_dt",
            "end_dt",
            "thumb_file",
        ]
        labels = {
            "title": "상품명",
            "contents": "상품내용",
            "type": "편의시설",
            "address": "주소",
            "start_dt": "상품시작일",
            "end_dt": "상품종료일",
            "thumb_file": "상품이미지",
        }

    type = forms.ModelMultipleChoiceField(
        queryset=RoomType.objects.all(), widget=forms.CheckboxSelectMultiple
    )


class MakeRoom(forms.ModelForm):
    class Meta:

        model = Room
        fields = ["room_name", "price"]
        labels = {"room_name": "객실 이름", "price": "객실 가격"}
