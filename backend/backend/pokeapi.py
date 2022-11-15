import requests


# This is where we will place all the logic to retrieve the data we need from the pokemon API and format it to a form
# that will be useful to see in the UI.
def get_pokemon():
    response = requests.get("https://pokeapi.co/api/v2/pokemon/?limit=150")
    json = response.json()
    pokemon = json['results']
    hydrated_pokemon = []
    for p in pokemon:
        hydration_res = requests.get(p['url'])
        hydration_json = hydration_res.json()
        sprite = hydration_json['sprites']['front_default']
        hydrated_pokemon.append({'name': p['name'], 'sprite': sprite})

    return {'pokemon': hydrated_pokemon}
