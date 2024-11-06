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
from game.models import Pokemon  # Certifique-se de que a importação está correta
from .fetch_pokemon import fetch_pokemon_data  # Importe a função fetch_pokemon_data

def populate_db(request):
    # Use a função fetch_pokemon_data para buscar os dados
    pokemon_data = fetch_pokemon_data()

    # Popule o banco de dados com os dados obtidos
    for data in pokemon_data:
        Pokemon.objects.create(
            name=data['name'],
            image=data['image'],
            evolution_chain=str(data['evolution_chain'])  # Armazene como uma string (ou JSON se preferir)
        )

    return HttpResponse("Banco de dados populado com sucesso!")

