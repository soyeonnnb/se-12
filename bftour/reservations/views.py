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

#For booking the room

# # 상품 예약
# @login_required(login_url='/user')
# def make_reservation(request):
#     if request.method =="POST":

#         room_id = request.POST['room_id']
        
#         room = Room.objects.all().get(room_name)
#         #for finding the reserved rooms on this time period for excluding from the query set
#         for each_reservation in Reservation.objects.all().filter(room = room):
#             if str(each_reservation.check_in) < str(request.POST['check_in']) and str(each_reservation.check_out) < str(request.POST['check_out']):
#                 pass
#             elif str(each_reservation.check_in) > str(request.POST['check_in']) and str(each_reservation.check_out) > str(request.POST['check_out']):
#                 pass
#             else:
#                 messages.warning(request,"Sorry This Room is unavailable for Booking")
#                 return redirect("homepage")
            
#         current_user = request.user
#         reservation_id = str(room_id) + str(datetime.datetime.now())

#         reservation = Reservation()
#         room_object = Room.objects.all().get(id=room_id)
#         room_object.status = '2'
        
#         user_object = User.objects.all().get(username=current_user)

#         Reservation.user = user_object
#         Reservation.room = room_object
#         Reservation.check_in = request.POST['check_in']
#         Reservation.check_out = request.POST['check_out']

#         Reservation.save()

#         messages.success(request,"Congratulations! Booking Successfull")

#         return redirect("homepage")
#     else:
#         return HttpResponse('Access Denied')

class CreateReservationView(user_mixin.LoggedInOnlyView, CreateView):
    model = models.Reservation 
    context_object_name = "reservation"
    form_calss = forms.ReservationForm
    success_url = reverse_lazy("reviews:reservation")
    template_name = "reservations/reservation_form.html"
    
    def form_valid(self, form):
        messages.success(self.request, 'form is valid')
        form.instance.user = self.request.user 
        form.save()

    def get_success_url(self):
        messages.success(self.request, 'Reservation Added Successfully')
        return reverse("reviews:reservation")
    
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
    success_url = reverse_lazy("reviews:reservation")
    template_name = "reservations/reservation_form.html"

    def get_context_data(self, **kwargs):
        context = super(UpdateReservationView, self).get_context_data(**kwargs)
        context["page_name"] = "예약 수정"
        context["reservation"] = models.Reservation.objects.get(pk=self.kwargs["pk"])
        # .reservation
        return context
    
# 예약 삭제 (코드작성완료)
class DeleteReservationView(user_mixin.LoggedInOnlyView, DeleteView):

    model = models.Reservation 
    context_object_name = "reservations"

    def get_success_url(self):
        return reverse_lazy("reservations:reservation_list")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
    

        
        

    



