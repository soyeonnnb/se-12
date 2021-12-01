from django.shortcuts import render, redirect

from . import forms
from reservations import models as reservations_model

# 아직 reservation과 합치기 전이므로 임의의 내 reservation을 보여주는 템플릿 생성
def view_reservation(request):
    user = request.user
    reservation_list = reservations_model.Reservation.objects.filter(user=user)
    return render(
        request, "reviews/reservation.html", {"reservation_list": reservation_list}
    )


def make_review(request, pk):
    reservation = reservations_model.Reservation.objects.get(
        pk=pk
    )  # order table에서 pk값으로 필요한 인스턴스를 가져옴
    user = request.user  # user는 요청을 보낸 유저
    if reservation.user != user:  # order 에 fk로 있는 user와 요청을 보낸 유저가 다르다면
        return redirect("users:home")
    if request.method == "POST":
        form = forms.CreateReviewForm(request.POST)  # 사용자가 입력한 폼을 가져옴
        if form.is_valid():
            finished_form = form.save(commit=False)
            finished_form.user = request.user  # 폼에 없는 요소들을 채워줌
            finished_form.reservation = reservation
            finished_form.room = reservation.room
            finished_form.save()
            return redirect("reviews:reservation")
    else:
        form = forms.CreateReviewForm()
    return render(
        request,
        "reviews/review_create.html",
        {"form": form, "reservation": reservation},
    )
