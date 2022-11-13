import requests
pokemon_routes_one_to_thirteen = []

# We're going to say we want our full team assembled by Gym 4, or by about route 12 or 13.
# So we need the list of pokemon you can encounter from routes 1 - 13.

# This gets us a list of the types of pokemon you can encounter on a specified route. It will also add them to an
# empty array, which we can use to collect all pokemon available in locations up to Gym 4.

def pokemon_route_encounters():
    response = requests.get("https://pokeapi.co/api/v2/location-area/295/")
    area = response.json()
    encounters = area['pokemon_encounters']
    for e in encounters:
        pokemon = e['pokemon']
        pokemon_routes_one_to_thirteen.append((pokemon['name']))

# Gets a list of all game types, including pokemon colosseum.
def pokemon_game_version():
    response = requests.get("https://pokeapi.co/api/v2/version/")
    version = response.json()
    game = version['results']
    for g in game:
        game_version = g['name']

# Gets a list of locations.
def list_of_locations():
    response = requests.get("https://pokeapi.co/api/v2/location/")
    location = response.json()
    area_name = location['results']
    for a in area_name:
        name = a['name']