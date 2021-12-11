from django.shortcuts import render, redirect
from django.views.generic import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

from . import forms
from . import models
from users import mixins as user_mixin
from reservations import models as reservation_model


@login_required
def make_review(request, pk):
    reservation = reservation_model.Reservation.objects.get(pk=pk)
    user = request.user
    if reservation.user != user:
        return redirect("users:home")
    if request.method == "POST":
        form = forms.ReviewForm(request.POST)
        if form.is_valid():
            finished_form = form.save(commit=False)
            finished_form.user = request.user
            finished_form.reservation = reservation
            finished_form.room = reservation.room
            finished_form.save()
            return redirect("reservations:reservation_list")
    else:
        form = forms.ReviewForm()
    return render(
        request,
        "reviews/review_form.html",
        {"form": form, "reservation": reservation, "page_name": "리뷰 등록"},
    )


class UpdateReview(user_mixin.LoggedInOnlyView, UpdateView):

    model = models.Review
    form_class = forms.ReviewForm
    success_url = reverse_lazy("reviews:view")
    template_name = "reviews/review_form.html"

    def get_context_data(self, **kwargs):
        context = super(UpdateReview, self).get_context_data(**kwargs)
        context["page_name"] = "리뷰 수정"
        context["reservation"] = models.Review.objects.get(
            pk=self.kwargs["pk"]
        ).reservation
        return context


@login_required
def view_reviews(request):
    user = request.user
    review_list = models.Review.objects.filter(user=user)
    return render(request, "reviews/review_list.html", {"review_list": review_list})


class DeleteReview(user_mixin.LoggedInOnlyView, DeleteView):

    model = models.Review
    context_object_name = "reviews"

    def get_success_url(self):
        return reverse_lazy("reviews:view")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
