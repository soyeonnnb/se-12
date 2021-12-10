import datetime
from django.contrib.auth.decorators import login_required
from django.http import Http404, request
from django.views.generic import (
    View,
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

from . import models
from . import forms
from rooms import models as rooms_model

from users import mixins as user_mixin


@login_required
def view_reservations(request):
    user = request.user
    reservation_list = models.Reservation.objects.filter(user=user)
    return render(
        request,
        "reservations/reservation_list.html",
        {"reservations": reservation_list},
    )


class CreateReservationView(user_mixin.LoggedInOnlyView, CreateView):

    model = models.Reservation
    context_object_name = "reservation"
    form_class = forms.ReservationForm
    template_name = "reservations/reservation_form.html"

    def get_context_data(self, **kwargs):
        context = super(CreateReservationView, self).get_context_data(**kwargs)
        context["page_name"] = "예약 하기"
        context["room"] = rooms_model.Room.objects.get(pk=self.kwargs["room_pk"])
        # .reservation
        return context

    def form_valid(self, form):
        messages.success(self.request, "form is valid")
        room = rooms_model.Room.objects.get(pk=self.kwargs.get("room_pk"))
        form.instance.user = self.request.user
        form.instance.room = room
        form.instance.hotel = room.hotel
        form.save()
        return super(CreateReservationView, self).form_valid(form)

    def get_success_url(self):
        messages.success(self.request, "Reservation Added Successfully")
        return reverse_lazy("reservations:reservation_list")


# 예약 수정
class UpdateReservationView(user_mixin.LoggedInOnlyView, UpdateView):
    model = models.Reservation
    form_class = forms.ReservationForm
    success_url = reverse_lazy("reservations:reservation_list")
    template_name = "reservations/reservation_form.html"

    def get_context_data(self, **kwargs):
        context = super(UpdateReservationView, self).get_context_data(**kwargs)
        context["page_name"] = "예약 수정"
        context["reservation"] = models.Reservation.objects.get(pk=self.kwargs["pk"])
        # .reservation
        return context


# 예약 삭제
class DeleteReservationView(user_mixin.LoggedInOnlyView, DeleteView):

    model = models.Reservation
    context_object_name = "reservations"

    def get_success_url(self):
        return reverse_lazy("reservations:reservation_list")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
