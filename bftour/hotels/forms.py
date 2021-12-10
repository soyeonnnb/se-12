from django import forms
from .models import Hotel, RoomType
from rooms.models import Room

from . import models


class MakeHotel(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = [
            "mem_seq",
            "title",
            "contents",
            "type",
            "address",
            "start_dt",
            "end_dt",
            "thumb_file",
        ]
        labels = {
            "mem_seq": "등록자",
            "title": "상품명",
            "contents": "상품내용",
            "type" :"편의시설",
            "address": "주소",
            "start_dt": "상품시작일",
            "end_dt": "상품종료일",
            "thumb_file": "상품이미지",
        }

#class MakeType(forms.ModelForm):
        type = forms.ModelChoiceField(label='편의시설',queryset= models.RoomType.objects.all(), empty_label="Any Kind", required=False)


class MakeRoom(forms.ModelForm):
    class Meta:

        model = Room
        fields = ["room_name", "price"]
        labels = {"room_name": "객실 이름", "price": "객실 가격"}
