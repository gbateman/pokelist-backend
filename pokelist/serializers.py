from .models import Pokemon
from rest_framework import serializers

class PokemonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pokemon
        fields = ('pokemon_id', 'name', 'location_area_encounters')
