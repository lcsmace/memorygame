# game/fetch_pokemon.py
import requests

def fetch_pokemon_data():
    pokemon_data = []
    
    # Extrair os primeiros 151 Pokémon
    for id in range(1, 152):
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{id}')
        if response.status_code == 200:
            data = response.json()
            species_url = data['species']['url']
            evolution_chain = fetch_evolution_chain(species_url)

            # Adicionar dados ao array
            pokemon_data.append({
                'name': data['name'],
                'image': data['sprites']['front_default'],
                'evolution_chain': evolution_chain
            })
    
    return pokemon_data

def fetch_evolution_chain(species_url):
    # Obter o URL da espécie e buscar a cadeia de evolução
    species_response = requests.get(species_url)
    species_data = species_response.json()
    evolution_chain_url = species_data['evolution_chain']['url']

    evolution_response = requests.get(evolution_chain_url)
    evolution_data = evolution_response.json()
    
    chain = []
    current = evolution_data['chain']
    
    while current:
        # Obter o URL da espécie atual para verificar o ID
        species_name = current['species']['name']
        species_info_url = current['species']['url']
        species_info_response = requests.get(species_info_url)
        species_info_data = species_info_response.json()
        
        # Verificar se o ID é menor ou igual a 151
        species_id = species_info_data['id']
        if species_id <= 151:
            chain.append(species_name)
        
        # Passar para a próxima evolução se houver
        if current['evolves_to']:
            current = current['evolves_to'][0]
        else:
            current = None
    
    return chain