from django.urls import path
from . import views
from .views import populate_db 

urlpatterns = [
    path('', views.home, name='home'),  # View que trata a URL raiz
    path('pokemon/', views.pokemon_list, name='pokemon_list'),
    path('populate-db/', populate_db, name='populate_db'),
]
