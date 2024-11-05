# game/store_pokemon.py
from .db_connection import get_mongo_collection

def store_pokemon_data(pokemon_data):
    collection = get_mongo_collection()

    collection.delete_many({})

    # Inserir todos os dados no MongoDB
    if pokemon_data:
        collection.insert_many(pokemon_data)
        print(f"{len(pokemon_data)} Pokémon inseridos no banco de dados.")