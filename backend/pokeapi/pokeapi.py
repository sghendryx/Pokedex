import requests
from pokeapi.models import Region, Location, Area


# This is where we will place all the logic to retrieve the data we need from the pokemon API and format it to a form
# that will be useful to see in the UI.

# Adds Pokemon you encounter's URLs in a location_area to the empty array pokemon_urls 
def pokemon_route_encounters():
    response = requests.get("https://pokeapi.co/api/v2/location-area/kanto-route-28-area/")
    area = response.json()
    encounters = area['pokemon_encounters']
    pokemon_names = []
    for e in encounters:
        pokemon = e['pokemon']
        pokemon_names.append(pokemon['name'])

    return pokemon_names


# Gets a Pokemon's name, its sprite, and its types from the Pokemons in the specified location area.
def get_pokemon():
    pokemon_names = pokemon_route_encounters()
    hydrated_pokemon = []
    for name in pokemon_names:
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{name}')
        hydration_json = response.json()
        sprite = hydration_json['sprites']['front_default']
        type = hydration_json['types']
        hydrated_pokemon.append({'name': name, 'sprite': sprite, 'type': type})

    return {'pokemon': hydrated_pokemon}


def get_regions():
    regions = Region.objects.all()
    response = {'regions': []}
    for r in regions:
        response['regions'].append({'name': r.name, 'poke_id': r.poke_id})
    return response


def get_locations(region_poke_id):
    locations = Location.objects.filter(region__poke_id=region_poke_id)
    response = {'locations': []}
    for l in locations:
        response['locations'].append({'name': l.name, 'poke_id': l.poke_id})
    return response


def test():
    regions = Region.objects.all()
    print(regions)
    return get_pokemon()
