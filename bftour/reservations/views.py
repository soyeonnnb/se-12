import datetime
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.views.generic import View, ListView, CreateView, DetailView
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from rooms import models as room_models
from reviews import forms as review_forms
from . import models
from . import forms

class CreateError(Exception):
    pass


# ------ MIXINS ------ #

class ReservationViewMixin(object):
    model = models.Reservation
    form_class = forms.ReservationForm
    
# ------ MODEL VIEWS ------ #

class ReservationCreateView(ReservationViewMixin, CreateView):
    """View to create a new ``Reservation`` instance."""
    def get_success_url(self):
        return reverse('reservation_detail', kwargs={'pk': self.object.pk})

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(ReservationCreateView, self).get_form_kwargs(
            *args, **kwargs)
        if self.request.user.is_authenticated():
            kwargs.update({'user': self.request.user})
        # else :
        return kwargs

class ReservationDetailView(ReservationViewMixin, DetailView):
    """View to display a ``Booking`` instance."""
    def dispatch(self, request, *args, **kwargs):
        self.kwargs = kwargs
        self.object = self.get_object()
        if self.request.user.is_authenticated():
            # If user doesn't own the booking forbid access
            if not self.object.user == request.user:
                raise Http404
        # else
        return super(ReservationViewMixin, self).dispatch(request, *args, **kwargs)

class ReservationListView(ReservationViewMixin, ListView):
    """View to display all ``Reservation`` instances of one user."""
    @login_required
    def dispatch(self, request, *args, **kwargs):
        return super(ReservationViewMixin, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return self.request.user.reservations.all()



# @login_required
# def make_reservation(request, pk):
#     user = request.user
#     if reservation.user != user:
#         return redirect("users:home")
#     if request.method == "POST":
#         form = forms.ReservationForm(request.POST)
#         if form.is_valid():
#             finished_form = form.save(commit=False)
#             finished_form.user = request.user
#             finished_form.reservation = reservation
#             finished_form.room = reservation.room
#             finished_form.save()
#             return redirect("reviews:reservation")
#     else:
#         form = forms.ReservationForm()
#     return render(
#         request,
#         "reviews/review_form.html",
#         {"form": form, "reservation": reservation, "page_name": "예약 상세페이지"},
#     )
#     return redirect(reverse("reservations:detail", kwargs={"pk": reservation.pk}))

# @login_required
# def create(request, room): # 수정
#     try:
#         room = room_models.Room.objects.get(pk=room)
#         raise CreateError()
#     except (room_models.Room.DoesNotExist, CreateError):
#         messages.error(request, "Can't Reserve That Room")
#         return redirect(reverse("core:home"))
#     except models.BookedDay.DoesNotExist:
#         reservation = models.Reservation.objects.create(
#             user=request.user,
#             room=room,
#             check_in=date_obj, # 여기
#             check_out=date_obj + datetime.timedelta(days=1), # 수정
#         )
#         return redirect(reverse("reservations:detail", kwargs={"pk": reservation.pk}))


# class ReservationDetailView(View):
#     def get(self, *args, **kwargs):
#         pk = kwargs.get("pk")
#         reservation = models.Reservation.objects.get_or_none(pk=pk)
#         if not reservation or (
#             reservation.user != self.request.user
#             and reservation.room.host != self.request.user
#         ):
#             raise Http404()
#         form = review_forms.ReviewForm()
#         return render(
#             self.request,
#             "reservations/detail.html",
#             {"reservation": reservation, "form": form},
#         )

# class UpdateReview(user_mixin.LoggedInOnlyView, UpdateView):

#     model = models.Review
#     form_class = forms.ReviewForm
#     success_url = reverse_lazy("reviews:view")
#     template_name = "reviews/review_form.html"

#     def get_context_data(self, **kwargs):
#         context = super(UpdateReview, self).get_context_data(**kwargs)
#         context["page_name"] = "리뷰 수정"
#         context["reservation"] = models.Review.objects.get(
#             pk=self.kwargs["pk"]
#         ).reservation
#         return context



# def edit_reservation(request, pk, verb):
#     reservation = models.Reservation.objects.get_or_none(pk=pk)
#     if not reservation or (
#         reservation.user != request.user
#     ):
#         raise Http404()
#     if verb == "confirm":
#         reservation.status = models.Reservation.STATUS_CONFIRMED
#     elif verb == "cancel":
#         reservation.status = models.Reservation.STATUS_CANCELED
#         models.BookedDay.objects.filter(reservation=reservation).delete()
#     reservation.save()
#     messages.success(request, "Reservation Updated")
#     return redirect(reverse("reservations:detail", kwargs={"pk": reservation.pk}))

# @login_required
# def make_review(request, pk):
#     reservation = reservation_model.Reservation.objects.get(pk=pk)
#     user = request.user
#     if reservation.user != user:
#         return redirect("users:home")
#     if request.method == "POST":
#         form = forms.ReviewForm(request.POST)
#         if form.is_valid():
#             finished_form = form.save(commit=False)
#             finished_form.user = request.user
#             finished_form.reservation = reservation
#             finished_form.room = reservation.room
#             finished_form.save()
#             return redirect("reviews:reservation")
#     else:
#         form = forms.ReviewForm()
#     return render(
#         request,
#         "reviews/review_form.html",
#         {"form": form, "reservation": reservation, "page_name": "리뷰 등록"},
#     )




# @login_required
# def view_reviews(request):
#     user = request.user
#     review_list = models.Review.objects.filter(user=user)
#     return render(request, "reviews/review_list.html", {"review_list": review_list})


# class DeleteReview(user_mixin.LoggedInOnlyView, DeleteView):

#     model = models.Review
#     context_object_name = "reviews"

#     def get_success_url(self):
#         return reverse_lazy("reviews:view")

#     def get(self, request, *args, **kwargs):
#         return self.post(request, *args, **kwargs)
