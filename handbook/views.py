from django.shortcuts import render, HttpResponse
from .models import GameRace, GameWeapon, GameArmor
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
        "heroes": [pickle.loads(bytes.fromhex(request.session.get(hid))) for hid in hero_list]
    }

    return render(request, "handbook/heroes.html", variables)


def new_hero(request) -> HttpResponse:
    hero_data = {
        "uid": str(uuid.uuid4()),
        "name": "Unknown",
        "lvl": 1,
        "race": "",
        "class": "",
        "hits": [0, 0],
        "energy": [0, 0]
    }
    request.session[hero_data["uid"]] = pickle.dumps(hero_data).hex()

    variables = {
        "name": "new_hero",
        "title": "Unknown",
        "show_bg": True,
        "hero_data": hero_data
    }

    return render(request, "closed.html", {})# "hero_page.html", variables)



def races(request) -> HttpResponse:
    all_races = GameRace.objects.all()
    variables = {
        "name": "races",
        "title": "Races",
        "header": "Расы и происхождения",
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



#def classes(request) -> HttpResponse:
#    #all_classes = GameSkill.objects.all()
#    context = {
#        "all_classes": None #all_classes,
#        # "img_path": {race.name_eng: f"/images/races/{race.name_eng}.png".replace(" ", "") for race in all_races}
#    }
#    return render(request, "handbook/classes.html", context)


#def weapons(request) -> HttpResponse:
#    all_weapons= GameWeapon.objects.all()
#    context = {
#        "all_weapons": all_weapons,
#    }
#    return render(request, "handbook/weapons.html", context)


#def armor(request) -> HttpResponse:
#    all_armor = GameArmor.objects.all()
#    context = {
#        "all_armor": all_armor
#    }
#    return render(request, "handbook/armor.html", context)

