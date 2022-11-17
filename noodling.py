import requests

# We're going to say we want our full team assembled by Gym 4, or by about route 10 or the rock tunnel.
# So we need the list of Pokemon you can encounter from routes 1 - rock-tunnel. Later I think we should
# put all the routes in order for each game, but this is a good starting point.

early_routes = ['kanto-route-1', 'kanto-route-2', 'viridian-forest', 'kanto-route-3',
                'mt-moon', 'kanto-route-4', 'kanto-route-24', 'kanto-route-25',
                'kanto-route-5', 'kanto-route-6', 'kanto-route-10', 'rock-tunnel']

encounter_location_urls = []
for place in early_routes:
    response = requests.get(f'https://pokeapi.co/api/v2/location/{place}/')
    location_details = response.json()
    location_areas = location_details['areas']
    for areas in location_areas:
        location_area_urls = areas['url']
        encounter_location_urls.append(location_area_urls)

#  This gets us a list of the types of pokemon you can encounter on a specified route. It will also add them to an
#  empty early_pokemon array, which we can use to collect all pokemon available in locations up to Gym 4.

early_pokemon = []
for url in encounter_location_urls:
    response = requests.get(f'{url}')
    area = response.json()
    encounters = area['pokemon_encounters']
    for e in encounters:
        early_pokemon.append(e['pokemon'])

print(early_pokemon)

# # Gets a list of all game types, including pokemon colosseum.
# def pokemon_game_version():
#     response = requests.get("https://pokeapi.co/api/v2/version/")
#     version = response.json()
#     game = version['results']
#     for g in game:
#         game_version = g['name']

# # Gets a list of all Pokemon and assigns it to the variable {pokemon_name}.
# response = requests.get("https://pokeapi.co/api/v2/pokemon/")
# pokemon_list = response.json()
# pokemon = pokemon_list['results']
# for p in pokemon:
#     pokemon_name = p['name']

# Gets a list of all Pokemon in the Pokemon Yellow Pokedex and assigns it to the list pokemon_names.
# pokemon_names = []
# response = requests.get("https://pokeapi.co/api/v2/pokedex/2/")
# pokedex_entries = response.json()
# pokedex_pokemon = pokedex_entries['pokemon_entries']
# for p in pokedex_pokemon:
#     pokemon_names.append(p['pokemon_species']['name'])