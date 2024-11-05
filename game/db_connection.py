# game/db_connection.py
from pymongo import MongoClient
from .config import MONGO_URI

def get_mongo_collection():
    client = MongoClient(MONGO_URI)
    db = client.pokemon_database  # Nome do banco de dados
    return db.pokemon_collection  # Nome da coleção onde vamos armazenar os Pokémon