from django.shortcuts import render
from .models import Pokemon
import random

def home(request):
    return render(request, 'game/index.html')  # Certifique-se de ter o template 'home.html'


def pokemon_list(request):
    # Buscar todos os Pokémon salvos no banco de dados SQLite
    pokemon_data = list(Pokemon.objects.all().values('name', 'image', 'evolution_chain'))

    # Embaralhar a lista de Pokémon
    random.shuffle(pokemon_data)

    # Renderizar o template e passar os dados dos Pokémon embaralhados
    return render(request, 'game/index.html', {'pokemon_data': pokemon_data})

from django.http import HttpResponse
from myapp.models import MyModel  # Substitua pelo seu modelo

def populate_db(request):
    MyModel.objects.create(field1='Value1', field2='Value2')  # Adicione os dados que precisar
    return HttpResponse("Banco de dados populado com sucesso!")
