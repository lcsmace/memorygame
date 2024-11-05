
from django.shortcuts import render
from django.http import HttpResponse
from .fetch_pokemon import fetch_pokemon_data
from .store_pokemon import store_pokemon_data
from .db_connection import get_mongo_collection
import random  # Importa o módulo random para embaralhar

def pokemon_list(request):
    # Conectar ao MongoDB e buscar todos os Pokémon
    collection = get_mongo_collection()
    pokemon_data = list(collection.find())  # Busca todos os Pokémon do MongoDB
    
    # Embaralhar a lista de Pokémon
    random.shuffle(pokemon_data)
    
    # Renderizar o template e passar os dados dos Pokémon embaralhados
    return render(request, 'game/index.html', {'pokemon_data': pokemon_data})

def populate_pokemon(request):
    # Buscar dados da PokéAPI
    pokemon_data = fetch_pokemon_data()
    
    # Armazenar os dados no MongoDB
    store_pokemon_data(pokemon_data)

    return HttpResponse("Dados dos Pokémon extraídos e armazenados com sucesso no MongoDB.")