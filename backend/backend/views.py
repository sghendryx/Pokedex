from rest_framework.response import Response
from rest_framework.decorators import api_view
from . import pokeapi

@api_view(['GET'])
def get_pokemon(request):
    return Response(pokeapi.get_pokemon())
