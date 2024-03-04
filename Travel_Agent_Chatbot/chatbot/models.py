# chatbot/models.py

from django.db import models

class City(models.Model):
    name = models.CharField(max_length=255, unique=True)

class Distance(models.Model):
    from_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='distances_from')
    to_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='distances_to')
    distance = models.FloatField()

class FlightTime(models.Model):
    from_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='flight_times_from')
    to_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='flight_times_to')
    flight_time = models.CharField(max_length=50)

class TravelPackage(models.Model):
    name = models.CharField(max_length=255)
    destinations = models.ManyToManyField(City)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
