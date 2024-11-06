import requests
from .models import Pokemon
import json

def fetch_evolution_chain(species_url):
    # Obter o URL da espécie e buscar a cadeia de evolução
    species_response = requests.get(species_url, verify=False)
    species_data = species_response.json()
    evolution_chain_url = species_data['evolution_chain']['url']

    evolution_response = requests.get(evolution_chain_url, verify=False)
    evolution_data = evolution_response.json()
    
    chain = []
    current = evolution_data['chain']
    
    while current:
        species_name = current['species']['name']
        species_info_url = current['species']['url']
        species_info_response = requests.get(species_info_url, verify=False)
        species_info_data = species_info_response.json()
        
        species_id = species_info_data['id']
        if species_id <= 151:
            chain.append(species_name)
        
        if current['evolves_to']:
            current = current['evolves_to'][0]
        else:
            current = None
    
    return chain

def fetch_pokemon_data():
    for id in range(1, 152):
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{id}')
        if response.status_code == 200:
            data = response.json()
            species_url = data['species']['url']
            evolution_chain = fetch_evolution_chain(species_url)

            # Salvar no banco de dados usando Django ORM
            Pokemon.objects.update_or_create(
                name=data['name'],
                defaults={
                    'image': data['sprites']['front_default'],
                    'evolution_chain': json.dumps(evolution_chain)  # Serializa a cadeia de evolução como JSON
                }
            )
