from django.shortcuts import render, redirect, HttpResponse
from .models import GameRace, GameWeaponNew, GameArmorNew
import pickle
import uuid


### New views
def index(request) -> HttpResponse:
    variables = {
        "name": "index",
        "title": "Home",
        "show_bg": True
    }

    return render(request, "handbook/index.html", variables)


def heroes(request) -> HttpResponse:
    hero_list = request.session.keys()
    variables = {
        "name": "heroes",
        "title": "Heroes",
        "show_bg": True,
        "heroes": [pickle.loads(bytes.fromhex(request.session.get(hero_id))) for hero_id in hero_list]
    }

    return render(request, "handbook/heroes.html", variables)
 

def hero_page(request, hero_id: str) -> HttpResponse:
    hero_data = pickle.loads(bytes.fromhex(request.session.get(hero_id)))
    variables = {
        "name": "hero-page",
        "title": hero_data["name"],
        "show_bg": True,
        "hero_data": hero_data
    }

    return render(request, "handbook/hero-page.html", variables)


def new_hero(request) -> HttpResponse:
   hero_data = {
        "uid": str(uuid.uuid4()),
        "name": "Unknown",
        "lvl": 1,
        "race": "Unknown race",
        "class": "Unknown class",
        "hits": {"max": 0, "cur": 0},
        "energy": {"max": 0, "cur": 0}
    }
   request.session[hero_data["uid"]] = pickle.dumps(hero_data).hex()

   return redirect("handbook:hero-page", hero_id=hero_data["uid"])


def races(request) -> HttpResponse:
    all_races = GameRace.objects.all()
    variables = {
        "name": "races",
        "title": "Races",
        "header": "Игровые расы",
        "show_bg": True,
        "all_elements": all_races
    }

    return render(request, "handbook/races.html", variables)


def race_page(request, name_eng: str) -> HttpResponse:
    cur_race = GameRace.objects.get(name_eng=name_eng)
    variables = {
        "name": "race-page",
        "title": name_eng,
        "show_bg": False,
        "info": cur_race
    }

    return render(request, "handbook/race-page.html", variables)


def weapons(request) -> HttpResponse:
    all_weapons = GameWeaponNew.objects.all()
    variables = {
        "name": "item-table",
        "title": "Weapons",
        "header": "Оружие и Фокусировки",
        "show_bg": True,
        "columns": ["Название", "Урон", "Тип урона", "Вес", "Цена", "Особенности"],
        "fill": [[
            item.name, 
            f"{item.damage[0]}d{item.damage[1]}",
            item.damage_type, 
            f"{item.weight} фнт",
            f"{item.costs[0]}з {item.costs[1]}с {item.costs[2]}м",
            f"{', '.join(item.features)}"
        ] for item in all_weapons]
    }

    return render(request, "handbook/item-table.html", variables)


def armors(request) -> HttpResponse:
    all_armors = GameArmorNew.objects.all()
    variables = {
        "name": "item-table",
        "title": "Armors",
        "header": "Доспехи и Одежда",
        "show_bg": True,
        "columns": ["Название", "КД", "Материал", "Вес", "Цена"],
        "fill": [[
            item.name,
            item.ac,
            item.material,
            f"{item.weight} фнт",
            f"{item.costs[0]}з {item.costs[1]}с {item.costs[2]}м"
        ] for item in all_armors]
    }

    return render(request, "handbook/item-table.html", variables)

