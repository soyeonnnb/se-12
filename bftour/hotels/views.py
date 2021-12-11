import datetime
from django.shortcuts import get_object_or_404, render, redirect
from .models import Hotel
from .forms import MakeHotel, MakeRoom
from rooms.models import Room
from django.contrib import messages
from reservations import models as reservations_models

# Create your views here.
def my_hotel(request):
    user = request.user
    hotels = Hotel.objects.filter(mem_seq=user)
    check_in = datetime.date.today()
    check_out = datetime.date.today() + datetime.timedelta(days=1)
    context = {
        "hotels": hotels,
        "check_in": check_in,
        "check_out": check_out,
    }
    return render(request, "hotels/myhotel.html", context)


def my_hotel_reservation(request, pk):
    hotel = Hotel.objects.get(pk=pk)
    reservations = reservations_models.Reservation.objects.filter(hotel=pk)
    check_in = datetime.date.today()
    check_out = datetime.date.today() + datetime.timedelta(days=1)
    return render(
        request,
        "hotels/myreservation.html",
        {
            "hotel": hotel,
            "reservations": reservations,
            "check_in": check_in,
            "check_out": check_out,
        },
    )


def makehotels(request):
    if request.method == "POST":
        form = MakeHotel(request.POST, request.FILES)

        if form.is_valid():
            forms = form.save(commit=False)
            forms.mem_seq = request.user
            forms.reg_id = request.user.name
            forms.save()
            form.save_m2m()

        return redirect("hotels:my_hotel")
    else:
        form = MakeHotel()
    return render(request, "hotels/makehotel.html", {"form": form})


def viewhotel(request, hotel_pk, check_in, check_out):
    # 게시글(Post) 중 pk(primary_key)를 이용해 하나의 게시글(post)를 검색
    hotels = Hotel.objects.get(pk=hotel_pk)
    rooms = Room.objects.filter(hotel=hotels)
    # posting.html 페이지를 열 때, 찾아낸 게시글(post)을 post라는 이름으로 가져옴
    kwargs = {
        "hotels": hotels,
        "rooms": rooms,
        "check_in": check_in,
        "check_out": check_out,
    }
    return render(request, "hotels/viewhotel.html", kwargs)


def deletehotel(request, pk):
    hotels = Hotel.objects.get(id=pk)
    rooms = Room.objects.get(hotel_id=pk)
    hotels.delete()
    rooms.delete()
    return redirect("hotels:my_hotel")


def updatehotel(request, pk):
    hotel = get_object_or_404(Hotel, pk=pk)
    if request.method == "POST":
        form = MakeHotel(request.POST, request.FILES, instance=hotel)
        if form.is_valid():
            forms = form.save(commit=False)
            forms.reg_id = request.user.id
            forms.save()
        return redirect("hotels:my_hotel")
    else:
        form = MakeHotel(instance=hotel)
    return render(
        request,
        "hotels/makehotel.html",
        {"form": form, "pk": pk},
    )
