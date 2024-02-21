from django.urls import path
from . import views


app_name = "handbook"
urlpatterns = [
    ### New path
    path("", views.index, name="index"),
    path("heroes/", views.heroes, name="heroes"),
    path("heroes/<str:hero_id>/", views.hero_page, name="hero-page"),
    path("races/", views.races, name="races"),
    path("races/<str:name_eng>/", views.race_page, name="race-page"),

    path("weapons/", views.weapons, name="weapons"),
    path("armors/", views.armors, name="armors")
   ]
