from django.db import models


class Region(models.Model):
    name = models.CharField(max_length=50)
    poke_id = models.IntegerField()


class Location(models.Model):
    name = models.CharField(max_length=50)
    poke_id = models.IntegerField()
    region = models.ForeignKey(Region, on_delete=models.CASCADE)


class Area(models.Model):
    name = models.CharField(max_length=50)
    poke_id = models.IntegerField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
