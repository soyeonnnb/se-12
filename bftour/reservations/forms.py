from django import forms

from models import Reservation
    
class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ("check_in", "check_out", "request")
        
    def __init__(self, user=None, *args, **kwargs):
        self.user = user
        super(ReservationForm, self).__init__(*args, **kwargs)
        # fields that should remain blank / not required
        keep_blank = ["check_in", "check_out", "request"]
        # set all fields except the keep_blank ones to be required, since they
        # need to be blank=True on the model itself to allow creating Booking
        # instances without data
        # for name, field in self.fields.items():
        #     if name not in keep_blank:
        #         self.fields[name].required = True

    def save(self, *args, **kwargs):
        if not self.instance.pk:
            self.instance.user = self.user
            status_object, created = Reservation.STATUS_CHOICES.objects.get_or_create(
                slug=getattr(settings, 'BOOKING_STATUS_CREATED', 'pending'))
            self.instance.booking_status = status_object
        return super(ReservationForm, self).save(*args, **kwargs)

    