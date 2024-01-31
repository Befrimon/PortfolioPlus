from django.shortcuts import render, HttpResponse
from .models import GameRace, GameWeapon
import pickle
import uuid


def index(request) -> HttpResponse:
    return render(request, "handbook/index.html", {})


def races(request) -> HttpResponse:
    all_races = GameRace.objects.all()
    context = {
        "all_races": all_races,
        "img_path": {race.name_eng: f"/images/races/{race.name_eng}.png".replace(" ", "") for race in all_races}
    }
    return render(request, "handbook/races.html", context)


def race_page(request, name_eng: str) -> HttpResponse:
    race = GameRace.objects.get(name_eng=name_eng)
    context = {
        "name_rus": race.name_rus,
        "name_eng": race.name_eng.replace(" ", ""),
        "description": race.description,

        "info": {
            "title": {
                "countries": "Страны",
                "lands": "Территории",
                "languages": "Языки",
                "religions": "Религия"
            },
            "context": race.info
        },
        "create": race.create,
        "skills": race.skills,
        "spec": race.spec,
        "acting": race.acting,

        "base_bg": True
    }
    return render(request, "handbook/race_page.html", context)


def heroes(request) -> HttpResponse:
    hero_list = request.session.keys()

    context = {
        "heroes": [pickle.loads(bytes.fromhex(request.session.get(hid))) for hid in hero_list]
    }
    return render(request, "handbook/heroes.html", context)


def new_hero(request) -> HttpResponse:
    hero_id = str(uuid.uuid4())
    context = {
        "id": hero_id,
        "name": "New hero",
        "hp": [10, 10],
        "energy": [2, 2]
    }

    request.session[hero_id] = pickle.dumps(context).hex()

    return render(request, "handbook/hero.html", context)


def hero(request, hero_id: str) -> HttpResponse:
    hero_data = pickle.loads(bytes.fromhex(request.session.get(hero_id)))

    context = {
        "name": hero_data["name"],
        "hp": hero_data["hp"],
        "energy": hero_data["energy"]
    }

    return render(request, "handbook/hero.html", context)


def classes(request) -> HttpResponse:
    #all_classes = GameSkill.objects.all()
    context = {
        "all_classes": None #all_classes,
        # "img_path": {race.name_eng: f"/images/races/{race.name_eng}.png".replace(" ", "") for race in all_races}
    }
    return render(request, "handbook/classes.html", context)


def weapons(request) -> HttpResponse:
    all_weapons= GameWeapon.objects.all()
    context = {
        "all_weapons": all_weapons,
    }
    return render(request, "handbook/weapons.html", context)

