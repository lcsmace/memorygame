# game/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('populate/', views.populate_pokemon, name='populate_pokemon'),
    path('pokemon/', views.pokemon_list, name='pokemon_list'),  # Nova URL para listar os Pokémon
]