from django.shortcuts import render, redirect
from .forms import MakeRoom
from django.contrib import messages
from rooms.models import Room


def makeroom(request, pk):
    if request.method == "POST":
        room = MakeRoom(request.POST)
        print(pk)
        if room.is_valid():
            forms = room.save(commit=False)
            forms.hotel_id = pk
            forms.user_id = request.user.id
            forms.save()
        return render(request, "rooms/makeroom.html", {"room": room})
    else:
        room = MakeRoom()
    return render(request, "rooms/makeroom.html", {"room": room})


def deleteroom(request, pk, fk):
    rooms = Room.objects.get(id=pk)
    rooms.delete()
    #return redirect("hotel:viewhotel", kwargs={"pk": pk})
    return redirect("hotels:my_hotel")