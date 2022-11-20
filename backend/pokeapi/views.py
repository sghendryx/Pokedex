from rest_framework.response import Response
from rest_framework.decorators import api_view
from pokeapi import pokeapi


@api_view(['GET'])
def get_pokemon(request):
    return Response(pokeapi.get_pokemon())


@api_view(['GET'])
def test(request):
    return Response(pokeapi.test())


@api_view(['GET'])
def regions(request):
    return Response(pokeapi.get_regions())
