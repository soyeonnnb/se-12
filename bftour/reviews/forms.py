from django import forms

from . import models


class ReviewForm(forms.ModelForm):
    class Meta:
        model = models.Review
        fields = ("review", "rating")

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)

        self.fields["rating"].widget.attrs = {
            "max": 5,
            "min": 1,
        }
