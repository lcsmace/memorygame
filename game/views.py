from django.shortcuts import render
from .models import Pokemon
import random

def home(request):
    return render(request, 'game/home.html')  # Certifique-se de ter o template 'home.html'


def pokemon_list(request):
    # Buscar todos os Pokémon salvos no banco de dados SQLite
    pokemon_data = list(Pokemon.objects.all().values('name', 'image', 'evolution_chain'))

    # Embaralhar a lista de Pokémon
    random.shuffle(pokemon_data)

    # Renderizar o template e passar os dados dos Pokémon embaralhados
    return render(request, 'game/index.html', {'pokemon_data': pokemon_data})
