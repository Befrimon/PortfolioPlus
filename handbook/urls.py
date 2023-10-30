from django.urls import path
from . import views


app_name = "handbook"
urlpatterns = [
    path("", views.index, name="index"),
    path("races/", views.races, name="races"),
    path("races/<str:name_eng>/", views.race_page, name="race_page"),
    path("heroes/", views.heroes, name="heroes")
]
