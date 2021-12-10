from django import forms
from .models import Hotel
from rooms.models import Room


class MakeHotel(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = [
            "mem_seq",
            "title",
            "contents",
            "address",
            "start_dt",
            "end_dt",
            "pro_price",
            "thumb_file",
        ]
        labels = {
            "mem_seq": "등록자",
            "title": "상품명",
            "contents": "상품내용",
            "address": "주소",
            "start_dt": "상품시작일",
            "end_dt": "상품종료일",
            "pro_price": "상품가격",
            "thumb_file": "상품이미지",
        }


class MakeRoom(forms.ModelForm):
    class Meta:

        model = Room
        fields = ["room_name", "price"]
        labels = {"room_name": "객실 이름", "price": "객실 가격"}
