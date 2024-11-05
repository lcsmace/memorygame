# game/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('pokemon/', views.pokemon_list, name='pokemon_list'),  # Nova URL para listar os Pokémon
]