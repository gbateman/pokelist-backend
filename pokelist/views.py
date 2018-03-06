from .models import Pokemon
from rest_framework import viewsets
from .serializers import PokemonSerializer

class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all().order_by('pokemon_id')
    serializer_class = PokemonSerializer
