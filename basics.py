import requests

# We're going to say we want our full team assembled by Gym 4, or by about route 12 or 13.
# So we need the list of pokemon you can encounter from routes 1 - 13.

# Gets a list of all Pokemon in the Pokemon Yellow Pokedex and assigns it to the list pokemon_names.
pokemon_names = []
response = requests.get("https://pokeapi.co/api/v2/pokedex/2/")
pokedex_entries = response.json()
pokedex_pokemon = pokedex_entries['pokemon_entries']
for p in pokedex_pokemon:
    pokemon_names.append(p['pokemon_species']['name'])

# This retrieves all location area encounters for every Pokemon using the {pokemon_names} list that was just created.
# This includes ways to encounter them from all of the games, though, so it isn't quite what we need yet.
for pokemon in pokemon_names:
    response = requests.get("https://pokeapi.co/api/v2/pokemon/{pokemon}/encounters")
    area_encounters = response.json()

# We now need to find a list of all area_encounters available in Pokemon Yellow. We can do that by taking a list of
# all locations, find the locations that are from generation-i, and compare that to our encounter_locations from
# our pokemon in pokemon yellow list.

# Finds the name of all locations and adds their name to the location_names list.
location_names = []
response = requests.get("https://pokeapi.co/api/v2/location/")
locations = response.json()
names = locations['results']
for r in names:
    location_names.append(r['name'])

# Takes locations that are from generation-i and adds it to the list generation_one_locations.
generation_one_locations = []
for location in location_names:
    response = requests.get("https://pokeapi.co/api/v2/location/{location}/")
    location_details = response.json()
    game_indices = location_details['game_indices']
    for g in game_indices:
        generation_one_locations.append(g['generation']['name'])

print(generation_one_locations)

# location_names = locations['areas']['name']
# print(location_names)


# # This gets us a list of the types of pokemon you can encounter on a specified route. It will also add them to an
# # empty array, which we can use to collect all pokemon available in locations up to Gym 4.

# def pokemon_route_encounters():
#     response = requests.get("https://pokeapi.co/api/v2/location-area/295/")
#     area = response.json()
#     encounters = area['pokemon_encounters']
#     for e in encounters:
#         pokemon = e['pokemon']
#         pokemon_routes_one_to_thirteen.append((pokemon['name']))

# # Gets a list of all game types, including pokemon colosseum.
# def pokemon_game_version():
#     response = requests.get("https://pokeapi.co/api/v2/version/")
#     version = response.json()
#     game = version['results']
#     for g in game:
#         game_version = g['name']

# # Gets a list of locations.
# def list_of_locations():
#     response = requests.get("https://pokeapi.co/api/v2/location/")
#     location = response.json()
#     area_name = location['results']
#     for a in area_name:
#         name = a['name']

# # Gets a list of all Pokemon and assigns it to the variable {pokemon_name}.
# response = requests.get("https://pokeapi.co/api/v2/pokemon/")
# pokemon_list = response.json()
# pokemon = pokemon_list['results']
# for p in pokemon:
#     pokemon_name = p['name']
