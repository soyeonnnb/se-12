<<<<<<< HEAD
from django.shortcuts import render

# Create your views here.
=======
from django.shortcuts import render, redirect
from django.views.generic import UpdateView, DeleteView
from django.urls import reverse_lazy

from . import forms
from . import models
from reservations import models as reservations_model

# 아직 reservation과 합치기 전이므로 임의의 내 reservation을 보여주는 템플릿 생성
def view_reservations(request):
    user = request.user
    reservation_list = reservations_model.Reservation.objects.filter(user=user)
    return render(
        request, "reviews/reservation.html", {"reservation_list": reservation_list}
    )


def make_review(request, pk):
    reservation = reservations_model.Reservation.objects.get(pk=pk)
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
            return redirect("reviews:reservation")
    else:
        form = forms.ReviewForm()
    return render(
        request,
        "reviews/review_form.html",
        {"form": form, "reservation": reservation, "page_name": "리뷰 등록"},
    )


class UpdateReview(UpdateView):

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


def view_reviews(request):
    user = request.user
    review_list = models.Review.objects.filter(user=user)
    return render(request, "reviews/review_list.html", {"review_list": review_list})


class DeleteReview(DeleteView):

    model = models.Review
    context_object_name = "reviews"

    def get_success_url(self):
        return reverse_lazy("reviews:view")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
>>>>>>> parent of 08af834 (feat: login only 추가, setting.py에 login url 추가)
