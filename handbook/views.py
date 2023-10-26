from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import GameRace


def index(request):
    return render(request, "handbook/index.html", {})


def races(request):
    all_races = GameRace.objects.all()
    context = {
        "all_races": all_races
    }
    return render(request, "handbook/races.html", context)


def race_page(request, name_eng):
    race = GameRace.objects.get(name_eng=name_eng)
    context = {
        "name_rus": race.name_rus,
        "name_eng": race.name_eng,
        "description": race.description,

        "countries": ", ".join(race.countries),
        "lands": ", ".join(race.lands),
        "langs": ", ".join(race.langs),
        "religions": ", ".join(race.religions),

        "base_bg": True
    }
    return render(request, "handbook/race_page.html", context)
