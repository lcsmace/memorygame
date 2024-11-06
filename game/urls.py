from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # View que trata a URL raiz
    path('pokemon/', views.pokemon_list, name='pokemon_list'),
]
