# chatbot/models.py

from django.db import models

class TravelAgent(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

class TravelPackage(models.Model):
    agent = models.ForeignKey(TravelAgent, on_delete=models.CASCADE)
    destination = models.CharField(max_length=255)
    cost = models.DecimalField(max_digits=10, decimal_places=2)

class City(models.Model):
    name = models.CharField(max_length=255, unique=True)

class Distance(models.Model):
    source_city = models.ForeignKey(City, related_name='source_city', on_delete=models.CASCADE)
    destination_city = models.ForeignKey(City, related_name='destination_city', on_delete=models.CASCADE)
    distance_value = models.FloatField()

class FlightTime(models.Model):
    source_city = models.ForeignKey(City, related_name='flight_source_city', on_delete=models.CASCADE)
    destination_city = models.ForeignKey(City, related_name='flight_destination_city', on_delete=models.CASCADE)
    flight_time_hours = models.FloatField()
