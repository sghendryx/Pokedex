from rest_framework.response import Response
from rest_framework.decorators import api_view
from pokeapi import pokeapi


@api_view(['GET'])
def test(request):
    return Response(pokeapi.test())


@api_view(['GET'])
def regions(request):
    return Response(pokeapi.get_regions())


@api_view(['GET'])
def locations(request, region_poke_id):
    return Response(pokeapi.get_locations(region_poke_id))


@api_view(['GET'])
def areas(request, location_poke_id):
    return Response(pokeapi.get_areas(location_poke_id))


@api_view(['GET'])
def get_pokemon(request, area_poke_id):
    return Response(pokeapi.get_pokemon(area_poke_id))
