from django.shortcuts import render
from .models import GameRace, Heroes


def index(request):
    return render(request, "handbook/index.html", {})


def races(request):
    all_races = GameRace.objects.all()
    context = {
        "all_races": all_races,
        "img_path": {race.name_eng: f"/images/races/{race.name_eng}.png".replace(" ", "") for race in all_races}
    }
    return render(request, "handbook/races.html", context)


def race_page(request, name_eng):
    race = GameRace.objects.get(name_eng=name_eng)
    context = {
        "name_rus": race.name_rus,
        "name_eng": race.name_eng.replace(" ", ""),
        "description": race.description,

        "info": race.info,
        "spec": race.spec,
        "create": race.create,

        "base_bg": True
    }
    return render(request, "handbook/race_page.html", context)


def heroes(request):
    heroes = Heroes.objects.all()
    context = {
        "heroes": heroes
    }
    return render(request, "handbook/heroes.html", context)
