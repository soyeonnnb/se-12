from django.shortcuts import render
from django.views.generic import View
from hotels import models as hotels_model
from django.core.paginator import Paginator
from django.db.models import Q

from . import forms


def home(request):
    form = forms.SearchForm()
    return render(request, "core/home.html", {"form": form})


class SearchView(View):
    def get(self, request):
        if (
            request.GET.get("text")
            or request.GET.get("start")
            or request.GET.get("type")
        ):
            form = forms.SearchForm(request.GET)
            if form.is_valid():
                text = form.cleaned_data.get("text")
                types = form.cleaned_data.get("types")
                n_hotels = hotels_model.Hotel.objects.all()
                if text:
                    n_hotels = n_hotels.filter(
                        Q(title__icontains=text)
                        | Q(place__icontains=text)
                        | Q(address__icontains=text)
                    )
                for type in types:
                    n_hotels = n_hotels.filter(type=type)
                # 나중에 별점순으로 변경
                paginator = Paginator(n_hotels, 10, orphans=5)
                page = request.GET.get("page", 1)
                hotels = paginator.get_page(page)
                return render(
                    request,
                    "core/result.html",
                    {"form": form, "hotels": hotels},
                )
        else:
            form = forms.SearchForm()
        return render(
            request,
            "core/result.html",
            {"form": form},
        )
