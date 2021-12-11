from django.shortcuts import render
from django.views.generic import View
from django.core.paginator import Paginator
from django.db.models import Q
import datetime
from . import forms
from hotels import models as hotels_model
from reservations import models as reservations_model
from rooms import models as rooms_model


def home(request):
    form = forms.SearchForm()
    hotels = hotels_model.Hotel.objects.all().order_by("-reg_dt")
    check_in = datetime.date.today()
    check_out = datetime.date.today() + datetime.timedelta(days=1)
    kwargs = {
        "form": form,
        "type": type,
        "hotels": hotels,
        "check_in": check_in,
        "check_out": check_out,
    }
    return render(request, "core/home.html", kwargs)


class SearchView(View):
    def get(self, request):
        if request.GET.get("text"):
            form = forms.SearchForm(request.GET)
            if form.is_valid():
                text = form.cleaned_data.get("text")
                types = form.cleaned_data.get("types")
                check_in = form.cleaned_data.get("start")
                check_out = form.cleaned_data.get("end")
                n_rooms = rooms_model.Room.objects.all().order_by("hotel__reg_dt")
                if text:
                    n_rooms = n_rooms.filter(
                        Q(hotel__title__icontains=text)
                        | Q(hotel__address__icontains=text)
                    )
                type_args = {}
                for type in types:
                    type_args["hotel__type"] = type
                n_rooms = n_rooms.filter(**type_args)
                date_args = dict(
                    check_in__lte=check_out, check_out__gte=check_in
                )  # just for redability
                for room in n_rooms:
                    is_occupied = reservations_model.Reservation.objects.filter(
                        **date_args, room=room
                    ).exists()
                    if is_occupied:
                        n_rooms = n_rooms.exclude(pk=room.pk)
                # 나중에 별점순으로 변경
                paginator = Paginator(n_rooms, 10, orphans=5)
                page = request.GET.get("page", 1)
                rooms = paginator.get_page(page)
                return render(
                    request,
                    "core/result.html",
                    {
                        "form": form,
                        "rooms": rooms,
                        "check_in": check_in,
                        "check_out": check_out,
                    },
                )
        else:
            form = forms.SearchForm()
        return render(
            request,
            "core/result.html",
            {"form": form},
        )
