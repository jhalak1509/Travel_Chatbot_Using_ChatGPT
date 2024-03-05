import os
import django
from faker import Faker
from random import randint

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Travel_Agent_Chatbot.settings")

# Configure Django
django.setup()

from chatbot.models import City, Distance, FlightTime, TravelPackage, TravelAgent


fake = Faker()

def create_cities():
    fake = Faker()
    existing_city_names = set(City.objects.values_list('name', flat=True))

    for _ in range(1000):
        unique_city_name = fake.unique.city()
        while unique_city_name in existing_city_names:
            unique_city_name = fake.unique.city()
        
        City.objects.create(name=unique_city_name)

def create_distances():
    existing_distances_count = Distance.objects.count()
    required_distances_count = 1000 - existing_distances_count

    cities = City.objects.all()

    for _ in range(required_distances_count):
        source_city = fake.random_element(elements=cities)
        destination_city = fake.random_element(elements=cities.exclude(pk=source_city.pk))

        Distance.objects.create(
            source_city=source_city,
            destination_city=destination_city,
            distance_value=randint(100, 1000)
        )

def create_flight_times():
    existing_flight_times_count = FlightTime.objects.count()
    required_flight_times_count = 1000 - existing_flight_times_count

    cities = City.objects.all()

    for _ in range(required_flight_times_count):
        source_city = fake.random_element(elements=cities)
        destination_city = fake.random_element(elements=cities.exclude(pk=source_city.pk))

        FlightTime.objects.create(
            source_city=source_city,
            destination_city=destination_city,
            flight_time_hours=randint(1, 10)
        )

def create_travel_agents():
    existing_agents_count = TravelAgent.objects.count()
    required_agents_count = 1000 - existing_agents_count

    for _ in range(required_agents_count):
        TravelAgent.objects.create(name=fake.company())

def create_travel_packages():
    existing_packages_count = TravelPackage.objects.count()
    required_packages_count = 1000 - existing_packages_count

    travel_agents = TravelAgent.objects.all()
    cities = City.objects.all()

    for _ in range(required_packages_count):
        agent = fake.random_element(elements=travel_agents)
        destination = fake.random_element(elements=cities)

        TravelPackage.objects.create(
            agent=agent,
            destination=destination,
            
            cost=randint(500, 5000)
        )

if __name__ == '__main__':
    create_cities()
    create_distances()
    create_flight_times()
    create_travel_agents()
    create_travel_packages()
