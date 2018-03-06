from django.db import models

class Pokemon(models.Model):
    pokemon_id = models.IntegerField()
    name = models.CharField(max_length=200)
    location_area_encounters = models.CharField(max_length=200)
    def __str__(self):
        return self.name
