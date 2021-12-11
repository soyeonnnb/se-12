from django import forms
import datetime

from hotels import models as hotels_model


def tomorrow():
    return datetime.date.today() + datetime.timedelta(days=1)


class SearchForm(forms.Form):

    TYPE_CHOICES = hotels_model.RoomType.objects.all()

    text = forms.CharField()
    start = forms.DateField(initial=datetime.date.today)
    end = forms.DateField(initial=tomorrow())
    types = forms.ModelMultipleChoiceField(
        queryset=hotels_model.RoomType.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,

    )
