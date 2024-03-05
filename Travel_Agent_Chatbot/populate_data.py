import os
import django
from faker import Faker
from random import randint
from Travel_Agent_Chatbot.chatbot.models import City, Distance, FlightTime, TravelPackage, TravelAgent

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Travel_Agent_Chatbot.settings')
django.setup()

fake = Faker()

def create_cities():
    existing_cities_count = City.objects.count()
    required_cities_count = 1000 - existing_cities_count

    for _ in range(required_cities_count):
        City.objects.create(name=fake.city())

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
            flight_time_value=randint(1, 10)
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
            package_name=fake.word(),
            cost=randint(500, 5000)
        )

if __name__ == '__main__':
    create_cities()
    create_distances()
    create_flight_times()
    create_travel_agents()
    create_travel_packages()
