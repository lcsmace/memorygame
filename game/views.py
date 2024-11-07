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
    print("Iniciando a função populate_db")
    pokemon_data = fetch_pokemon_data()
    if not pokemon_data:
        print("Erro: Nenhum dado foi retornado por fetch_pokemon_data")
        return HttpResponse("Erro ao popular o banco de dados: Nenhum dado encontrado.")

    for data in pokemon_data:
        print(f"Inserindo Pokémon: {data['name']}")
        Pokemon.objects.create(
            name=data['name'],
            image=data['image'],
            evolution_chain=str(data['evolution_chain'])
        )
    return HttpResponse("Banco de dados populado com sucesso!")

