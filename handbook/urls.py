from django.urls import path
from . import views


app_name = "handbook"
urlpatterns = [
    path("", views.index, name="index"),
    
    path("races/", views.races, name="races"),
    path("races/<str:name_eng>/", views.race_page, name="race_page"),

    path("classes/", views.classes, name="classes"),
    #path("classes/<str:name_eng>/", views.skill_page, name="skill_page"),
    #path("classes/<str:name_eng>/", views.class_page, name="class_page"),

    path("heroes/", views.heroes, name="heroes"),
    path("heroes/new_hero/", views.new_hero, name="new_hero"),
    path("heroes/<str:hero_id>/", views.hero, name="hero"),

    path("weapons/", views.weapons, name="weapons"),
    #path("armor/", views.armor, name="armor"),
]
