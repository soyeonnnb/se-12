import datetime
from django.contrib.auth.decorators import login_required
from django.http import Http404, request
from django.views.generic import View, ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

from . import models
from . import forms

from users import mixins as user_mixin

@login_required
def view_reservations(request):
    user = request.user
    reservation_list = models.Reservation.objects.filter(user=user)
    return render(
        request, "reservations/reservation_list.html", {"reservations": reservation_list}
    )
    
class CreateReservationView(user_mixin.LoggedInOnlyView, CreateView):
    model = models.Reservation 
    context_object_name = "reservation"
    form_class = forms.ReservationForm
    template_name = "reservations/reservation_form.html"
    
    def form_valid(self, form):
        messages.success(self.request, 'form is valid')
        form.instance.user = self.request.user 
        form.save()

    def get_success_url(self):
        messages.success(self.request, 'Reservation Added Successfully')
        return reverse("reservations:reservation_list")
    
    # def get_form_kwargs(self):
    #     kwargs = super(CreateReservationView, self).get_form_kwargs()
    #     kwarsg['user'] = self.request.user
    #     return kwargs 
        
    # def form_valid(self, form):
    #     reservation = form.save(commit=False)
    #     reservation.
    
    # def dispatch(self, *args, **kwargs):
    #     return super(CreateReservationView, self).dispatch(*args, **kwargs)
    
    # def get_user_initial(self):
    #     return {'user_name': {request.user.name}, 
    #             'user_phone':{request.user.phone}, 
    #             'user_email':{request.user.email},
    #             }
    
    
    # def form_valid(self, form) :
    #     temp_reservation = form.save(commit=False)
    #     temp_reservation.user = self.request.user
    #     temp_reservation.save()
        
    #     return super().form_valid(form) 
    

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
    

        
        

    



