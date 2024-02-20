from django.urls import path
from . import views


app_name = "handbook"
urlpatterns = [
    ### New path
    path("", views.index, name="index"),
    path("heroes/", views.heroes, name="heroes"),
    path("races/", views.races, name="races"),
    path("races/<str:name_eng>/", views.race_page, name="race_page"),

   ]
