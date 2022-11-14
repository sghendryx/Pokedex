import requests
pokemon_routes_one_to_thirteen = []

# We're going to say we want our full team assembled by Gym 4, or by about route 12 or 13.
# So we need the list of pokemon you can encounter from routes 1 - 13.


# For this idea below, I'm trying to find the Location Areas in Pokemon Yellow. I think there
# are 732 total? But I'm not sure. I'm trying to take a range of numbers and input them to specify
# the Location Area ID in the Location Area API, and then if the version details return True (are == to Yellow), it adds
# that Location Area to the list pokemon_yellow_locations. It'll print the game version, but only for a while before
# it starts to error, and I haven't gotten the == yellow boolean to work yet.

# Creates a list from 1 to 732, which is the total routes available.
area_id = [*range(1, 732)]
yellow_location_areas = []

# For reach number in the list, it substitutes it into the API url.
for number in area_id:
    response = requests.get(f'https://pokeapi.co/api/v2/location-area/{number}/')
    version_details = response.json()
    encounters = version_details['encounter_method_rates']
    for n in encounters:
        version_details = n['version_details']
        for game in version_details:
            game_version = game['version']['name']
            print(game_version)


# Gets a list of all Pokemon and assigns it to the variable {pokemon_name}. Can I use this for the rest 
# of the script now?
response = requests.get("https://pokeapi.co/api/v2/pokemon/")
pokemon_list = response.json()
pokemon = pokemon_list['results']
for p in pokemon:
    pokemon_name = p['name']


# Gets a list of all Pokemon in the Pokemon Yellow Pokedex.
response = requests.get("https://pokeapi.co/api/v2/pokedex/2/")
pokedex_entries = response.json()
pokedex_pokemon = pokedex_entries['pokemon_entries']
for p in pokedex_pokemon:
    pokemon_species = p['pokemon_species']['name']


# This retrieves all location area encounters for every Pokemon using the variable {pokemon_name} that was just created.
# Or that was the idea-- I didn't get this to work either.

def find_location_areas(pokemon_name):
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}/')
    pokemon = response.json()
    location_area_encounters = pokemon['location_area_encounters']
    print(location_area_encounters)


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

