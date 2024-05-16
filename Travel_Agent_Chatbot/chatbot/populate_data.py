from sqlalchemy.orm import sessionmaker
from models import TravelAgent, TravelPackage, City, Airport, Flight
from datetime import datetime
from .database import engine, Base

Session = sessionmaker(bind=engine)
session = Session()

# Drop all existing tables
Base.metadata.drop_all(engine)

# Recreate tables
Base.metadata.create_all(engine)

# Insert statements for TravelAgents
agents_data = [
    {'name': 'Global Travel Inc.', 'location': 'New York'},
    {'name': 'Wanderlust Travels', 'location': 'London'},
    {'name': 'Adventures Abroad', 'location': 'Sydney'},
    {'name': 'Dream Destinations', 'location': 'Paris'},
    {'name': 'Sunshine Travel Agency', 'location': 'Los Angeles'},
    {'name': 'ExploreMore', 'location': 'Tokyo'},
    {'name': 'Journey Jockey', 'location': 'Rio de Janeiro'},
    {'name': 'Discover World', 'location': 'Cape Town'},
    {'name': 'Voyage Ventures', 'location': 'Toronto'},
    {'name': 'Aloha Travel Co.', 'location': 'Honolulu'},
    {'name': 'Safari Seekers', 'location': 'Nairobi'},
    {'name': 'Northern Lights Travel', 'location': 'Reykjavik'},
    {'name': 'Mediterranean Odyssey', 'location': 'Athens'},
    {'name': 'Tropical Treks', 'location': 'Bali'},
    {'name': 'Alpine Adventures', 'location': 'Zurich'},
    {'name': 'Magic Kingdom Travel', 'location': 'Orlando'},
    {'name': 'Spiritual Journeys', 'location': 'Varanasi'},
    {'name': 'Pacific Paradise', 'location': 'Fiji'},
    {'name': 'Amazon Expeditions', 'location': 'Manaus'},
    {'name': 'Polar Quest', 'location': 'Longyearbyen'},
]

for data in agents_data:
    agent = TravelAgent(**data)
    session.add(agent)

# Insert statements for TravelPackages
packages_data = [
    {'agent_id': 1, 'packagename': 'Big Apple Experience', 'description': 'Explore New York City in style.', 'destination': 'New York', 'cost': 1500.00, 'origin_city_id': 1, 'destination_city_id': 1, 'valid_from': datetime(2024, 3, 1), 'valid_to': datetime(2024, 12, 31)},
    {'agent_id': 2, 'packagename': 'London Calling', 'description': 'Discover the iconic landmarks of London.', 'destination': 'London', 'cost': 1800.00, 'origin_city_id': 2, 'destination_city_id': 2, 'valid_from': datetime(2024, 3, 1), 'valid_to': datetime(2024, 12, 31)},
    {'agent_id': 3, 'packagename': 'Down Under Adventure', 'description': 'Experience the wonders of Australia.', 'destination': 'Sydney', 'cost': 2500.00, 'origin_city_id': 3, 'destination_city_id': 3, 'valid_from': datetime(2024, 3, 1), 'valid_to': datetime(2024, 12, 31)},
    {'agent_id': 4, 'packagename': 'Parisian Getaway', 'description': 'Fall in love with the charm of Paris.', 'destination': 'Paris', 'cost': 2200.00, 'origin_city_id': 4, 'destination_city_id': 4, 'valid_from': datetime(2024, 3, 1), 'valid_to': datetime(2024, 12, 31)},
    {'agent_id': 5, 'packagename': 'California Dreaming', 'description': 'Explore the beauty of California.', 'destination': 'Los Angeles', 'cost': 1700.00, 'origin_city_id': 5, 'destination_city_id': 5, 'valid_from': datetime(2024, 3, 1), 'valid_to': datetime(2024, 12, 31)},
    {'agent_id': 6, 'packagename': 'Tokyo Discovery', 'description': 'Immerse yourself in the energy of Tokyo.', 'destination': 'Tokyo', 'cost': 2800.00, 'origin_city_id': 6, 'destination_city_id': 6, 'valid_from': datetime(2024, 3, 1), 'valid_to': datetime(2024, 12, 31)},
    {'agent_id': 7, 'packagename': 'Brazilian Adventure', 'description': 'Experience the vibrant culture of Brazil.', 'destination': 'Rio de Janeiro', 'cost': 2000.00, 'origin_city_id': 7, 'destination_city_id': 7, 'valid_from': datetime(2024, 3, 1), 'valid_to': datetime(2024, 12, 31)},
    {'agent_id': 8, 'packagename': 'Cape Town Escapade', 'description': 'Discover the beauty of South Africa.', 'destination': 'Cape Town', 'cost': 2400.00, 'origin_city_id': 8, 'destination_city_id': 8, 'valid_from': datetime(2024, 3, 1), 'valid_to': datetime(2024, 12, 31)},
    {'agent_id': 9, 'packagename': 'Canadian Adventure', 'description': 'Explore the wilderness of Canada.', 'destination': 'Toronto', 'cost': 2100.00, 'origin_city_id': 9, 'destination_city_id': 9, 'valid_from': datetime(2024, 3, 1), 'valid_to': datetime(2024, 12, 31)},
    {'agent_id': 10, 'packagename': 'Aloha Hawaii', 'description': 'Relax on the beautiful beaches of Hawaii.', 'destination': 'Honolulu', 'cost': 2600.00, 'origin_city_id': 10, 'destination_city_id': 10, 'valid_from': datetime(2024, 3, 1), 'valid_to': datetime(2024, 12, 31)},
    {'agent_id': 1, 'packagename': 'Broadway Experience', 'description': 'Enjoy the best of Broadway in New York City.', 'destination': 'New York', 'cost': 1900.00, 'origin_city_id': 1, 'destination_city_id': 1, 'valid_from': datetime(2024, 3, 1), 'valid_to': datetime(2024, 12, 31)},
    {'agent_id': 2, 'packagename': 'Historic London Tour', 'description': 'Explore the rich history of London.', 'destination': 'London', 'cost': 2100.00, 'origin_city_id': 2, 'destination_city_id': 2, 'valid_from': datetime(2024, 3, 1), 'valid_to': datetime(2024, 12, 31)},
    {'agent_id': 3, 'packagename': 'Great Barrier Reef Adventure', 'description': 'Discover the wonders of the Great Barrier Reef.', 'destination': 'Sydney', 'cost': 2800.00, 'origin_city_id': 3, 'destination_city_id': 3, 'valid_from': datetime(2024, 3, 1), 'valid_to': datetime(2024, 12, 31)},
    {'agent_id': 4, 'packagename': 'Romantic Paris Getaway', 'description': 'Experience romance in the city of love.', 'destination': 'Paris', 'cost': 2500.00, 'origin_city_id': 4, 'destination_city_id': 4, 'valid_from': datetime(2024, 3, 1), 'valid_to': datetime(2024, 12, 31)},
    {'agent_id': 5, 'packagename': 'Golden State Adventure', 'description': 'Experience the highlights of California.', 'destination': 'Los Angeles', 'cost': 1900.00, 'origin_city_id': 5, 'destination_city_id': 5, 'valid_from': datetime(2024, 3, 1), 'valid_to': datetime(2024, 12, 31)},
    {'agent_id': 6, 'packagename': 'Tokyo City Tour', 'description': 'Explore the sights and sounds of Tokyo.', 'destination': 'Tokyo', 'cost': 2600.00, 'origin_city_id': 6, 'destination_city_id': 6, 'valid_from': datetime(2024, 3, 1), 'valid_to': datetime(2024, 12, 31)},
    {'agent_id': 7, 'packagename': 'Rio Carnival Experience', 'description': 'Witness the excitement of the Rio Carnival.', 'destination': 'Rio de Janeiro', 'cost': 2200.00, 'origin_city_id': 7, 'destination_city_id': 7, 'valid_from': datetime(2024, 3, 1), 'valid_to': datetime(2024, 12, 31)},
    {'agent_id': 8, 'packagename': 'Cape Winelands Tour', 'description': 'Indulge in wine tasting in Cape Town.', 'destination': 'Cape Town', 'cost': 2700.00, 'origin_city_id': 8, 'destination_city_id': 8, 'valid_from': datetime(2024, 3, 1), 'valid_to': datetime(2024, 12, 31)},
    {'agent_id': 9, 'packagename': 'Canadian Rockies Expedition', 'description': 'Explore the stunning Canadian Rockies.', 'destination': 'Toronto', 'cost': 2300.00, 'origin_city_id': 9, 'destination_city_id': 9, 'valid_from': datetime(2024, 3, 1), 'valid_to': datetime(2024, 12, 31)},
    {'agent_id': 10, 'packagename': 'Hawaiian Island Hopping', 'description': 'Explore multiple islands in Hawaii.', 'destination': 'Honolulu', 'cost': 2800.00, 'origin_city_id': 10, 'destination_city_id': 10, 'valid_from': datetime(2024, 3, 1), 'valid_to': datetime(2024, 12, 31)},
]

for data in packages_data:
    package = TravelPackage(**data)
    session.add(package)

# Insert statements for Cities
cities_data = [
    {'Cityname': 'New York', 'country': 'United States', 'timezone': 'America/New_York'},
    {'Cityname': 'London', 'country': 'United Kingdom', 'timezone': 'Europe/London'},
    {'Cityname': 'Sydney', 'country': 'Australia', 'timezone': 'Australia/Sydney'},
    {'Cityname': 'Paris', 'country': 'France', 'timezone': 'Europe/Paris'},
    {'Cityname': 'Los Angeles', 'country': 'United States', 'timezone': 'America/Los_Angeles'},
    {'Cityname': 'Tokyo', 'country': 'Japan', 'timezone': 'Asia/Tokyo'},
    {'Cityname': 'Rio de Janeiro', 'country': 'Brazil', 'timezone': 'America/Sao_Paulo'},
    {'Cityname': 'Cape Town', 'country': 'South Africa', 'timezone': 'Africa/Johannesburg'},
    {'Cityname': 'Toronto', 'country': 'Canada', 'timezone': 'America/Toronto'},
    {'Cityname': 'Honolulu', 'country': 'United States', 'timezone': 'Pacific/Honolulu'},
    {'Cityname': 'Nairobi', 'country': 'Kenya', 'timezone': 'Africa/Nairobi'},
    {'Cityname': 'Reykjavik', 'country': 'Iceland', 'timezone': 'Atlantic/Reykjavik'},
    {'Cityname': 'Athens', 'country': 'Greece', 'timezone': 'Europe/Athens'},
    {'Cityname': 'Bali', 'country': 'Indonesia', 'timezone': 'Asia/Makassar'},
    {'Cityname': 'Zurich', 'country': 'Switzerland', 'timezone': 'Europe/Zurich'},
    {'Cityname': 'Orlando', 'country': 'United States', 'timezone': 'America/New_York'},
    {'Cityname': 'Varanasi', 'country': 'India', 'timezone': 'Asia/Kolkata'},
    {'Cityname': 'Suva', 'country': 'Fiji', 'timezone': 'Pacific/Fiji'},
    {'Cityname': 'Manaus', 'country': 'Brazil', 'timezone': 'America/Manaus'},
    {'Cityname': 'Longyearbyen', 'country': 'Norway', 'timezone': 'Arctic/Longyearbyen'},
]

for data in cities_data:
    city = City(**data)
    session.add(city)

# Insert statements for Airports
airports_data = [
    {'city_id': 1, 'Airportname': 'John F. Kennedy International Airport', 'iata_code': 'JFK'},
    {'city_id': 2, 'Airportname': 'Heathrow Airport', 'iata_code': 'LHR'},
    {'city_id': 3, 'Airportname': 'Sydney Kingsford Smith International Airport', 'iata_code': 'SYD'},
    {'city_id': 4, 'Airportname': 'Paris Charles de Gaulle Airport', 'iata_code': 'CDG'},
    {'city_id': 5, 'Airportname': 'Los Angeles International Airport', 'iata_code': 'LAX'},
    {'city_id': 6, 'Airportname': 'Tokyo Haneda Airport', 'iata_code': 'HND'},
    {'city_id': 7, 'Airportname': 'Rio de Janeiro-Galeão International Airport', 'iata_code': 'GIG'},
    {'city_id': 8, 'Airportname': 'Cape Town International Airport', 'iata_code': 'CPT'},
    {'city_id': 9, 'Airportname': 'Toronto Pearson International Airport', 'iata_code': 'YYZ'},
    {'city_id': 10, 'Airportname': 'Daniel K. Inouye International Airport', 'iata_code': 'HNL'},
    {'city_id': 11, 'Airportname': 'Jomo Kenyatta International Airport', 'iata_code': 'NBO'},
    {'city_id': 12, 'Airportname': 'Keflavík International Airport', 'iata_code': 'KEF'},
    {'city_id': 13, 'Airportname': 'Athens International Airport', 'iata_code': 'ATH'},
    {'city_id': 14, 'Airportname': 'Ngurah Rai International Airport', 'iata_code': 'DPS'},
    {'city_id': 15, 'Airportname': 'Zurich Airport', 'iata_code': 'ZRH'},
    {'city_id': 16, 'Airportname': 'Orlando International Airport', 'iata_code': 'MCO'},
    {'city_id': 17, 'Airportname': 'Lal Bahadur Shastri Airport', 'iata_code': 'VNS'},
    {'city_id': 18, 'Airportname': 'Nadi International Airport', 'iata_code': 'NAN'},
    {'city_id': 19, 'Airportname': 'Eduardo Gomes International Airport', 'iata_code': 'MAO'},
    {'city_id': 20, 'Airportname': 'Svalbard Airport', 'iata_code': 'LYR'},
]

for data in airports_data:
    airport = Airport(**data)
    session.add(airport)

# Insert statements for Flights
flights_data = [
    {'departure_airport_id': 1, 'arrival_airport_id': 3, 'flight_duration': 20, 'operating_airlines': 'Delta Air Lines'},
    {'departure_airport_id': 2, 'arrival_airport_id': 4, 'flight_duration': 12, 'operating_airlines': 'British Airways'},
    {'departure_airport_id': 3, 'arrival_airport_id': 5, 'flight_duration': 15, 'operating_airlines': 'Qantas'},
    {'departure_airport_id': 4, 'arrival_airport_id': 6, 'flight_duration': 11, 'operating_airlines': 'Air France'},
    {'departure_airport_id': 5, 'arrival_airport_id': 7, 'flight_duration': 10, 'operating_airlines': 'American Airlines'},
    {'departure_airport_id': 6, 'arrival_airport_id': 8, 'flight_duration': 13, 'operating_airlines': 'Japan Airlines'},
    {'departure_airport_id': 7, 'arrival_airport_id': 9, 'flight_duration': 9, 'operating_airlines': 'LATAM Brasil'},
    {'departure_airport_id': 8, 'arrival_airport_id': 10, 'flight_duration': 11, 'operating_airlines': 'South African Airways'},
    {'departure_airport_id': 9, 'arrival_airport_id': 11, 'flight_duration': 14, 'operating_airlines': 'Air Canada'},
    {'departure_airport_id': 10, 'arrival_airport_id': 12, 'flight_duration': 11, 'operating_airlines': 'Hawaiian Airlines'},
    {'departure_airport_id': 11, 'arrival_airport_id': 13, 'flight_duration': 8, 'operating_airlines': 'Kenya Airways'},
    {'departure_airport_id': 12, 'arrival_airport_id': 14, 'flight_duration': 5, 'operating_airlines': 'Icelandair'},
    {'departure_airport_id': 13, 'arrival_airport_id': 15, 'flight_duration': 3, 'operating_airlines': 'Aegean Airlines'},
    {'departure_airport_id': 14, 'arrival_airport_id': 16, 'flight_duration': 6, 'operating_airlines': 'Garuda Indonesia'},
    {'departure_airport_id': 15, 'arrival_airport_id': 17, 'flight_duration': 8, 'operating_airlines': 'Swiss International Air Lines'},
    {'departure_airport_id': 16, 'arrival_airport_id': 18, 'flight_duration': 13, 'operating_airlines': 'JetBlue Airways'},
    {'departure_airport_id': 17, 'arrival_airport_id': 19, 'flight_duration': 9, 'operating_airlines': 'Air India'},
    {'departure_airport_id': 18, 'arrival_airport_id': 20, 'flight_duration': 6, 'operating_airlines': 'Fiji Airways'},
    {'departure_airport_id': 19, 'arrival_airport_id': 1, 'flight_duration': 4, 'operating_airlines': 'Azul Brazilian Airlines'},
    {'departure_airport_id': 20, 'arrival_airport_id': 2, 'flight_duration': 5, 'operating_airlines': 'SAS Scandinavian Airlines'},
]

for data in flights_data:
    flight = Flight(**data)
    session.add(flight)

# Commit changes and close session
session.commit()
session.close()







"""from sqlalchemy.orm import Session
import random
import string
from faker import Faker
from database import SessionLocal
from models import City, Airport, Flight, TravelAgent, TravelPackage

fake = Faker()

def generate_cities(db: Session, count: int = 50):
    cities = []
    for _ in range(count):
        city = City(
            Cityname=fake.city(),
            country=fake.country(),
            timezone=fake.timezone()
        )
        cities.append(city)
    db.bulk_save_objects(cities)
    db.commit()

def generate_airports(db: Session, count: int = 50):
    cities = db.query(City).all()
    airports = []
    iata_codes = set()  # Keep track of generated IATA codes
    for _ in range(count):
        # Generate a unique IATA code
        while True:
            # Generate a random 3-letter code
            iata_code = ''.join(random.choices(string.ascii_uppercase, k=3))
            if iata_code not in iata_codes:
                iata_codes.add(iata_code)
                break
        
        airport = Airport(
            city_id=random.choice(cities).id,
            Airportname=f"{fake.city()} International Airport",
            iata_code=iata_code
        )
        airports.append(airport)
    db.bulk_save_objects(airports)
    db.commit()

def generate_travel_agents(db: Session, count: int = 10):
    agents = []
    for _ in range(count):
        agent = TravelAgent(
            name=fake.company(),
            location=fake.city()
        )
        agents.append(agent)
    db.bulk_save_objects(agents)
    db.commit()

def generate_flights(db: Session, count: int = 180):
    airports = db.query(Airport).all()
    flights = []
    for _ in range(count):
        flight = Flight(
            departure_airport_id=random.choice(airports).id,
            arrival_airport_id=random.choice(airports).id,
            flight_duration=fake.random_int(min=1, max=18),  # Duration in hours
            operating_airlines=fake.company()
        )
        flights.append(flight)
    db.bulk_save_objects(flights)
    db.commit()

def generate_travel_packages(db: Session, count: int = 40):
    cities = db.query(City).all()
    agents = db.query(TravelAgent).all()
    packages = []
    for _ in range(count):
        origin_city = random.choice(cities)
        destination_city = random.choice(cities)
        while destination_city == origin_city:
            destination_city = random.choice(cities)

        package = TravelPackage(
            agent_id=random.choice(agents).id,
            packagename=f"{fake.word().capitalize()} Package",
            description=fake.text(),
            destination=destination_city.Cityname,
            cost=fake.random_number(digits=5),
            origin_city_id=origin_city.id,
            destination_city_id=destination_city.id,
            valid_from=fake.date_time_this_decade(before_now=True, after_now=False),
            valid_to=fake.date_time_this_decade(before_now=False, after_now=True)
        )
        packages.append(package)
    db.bulk_save_objects(packages)
    db.commit()

def main():
    db = SessionLocal()
    generate_cities(db)
    generate_airports(db)
    generate_travel_agents(db)
    generate_flights(db)
    generate_travel_packages(db)
    db.close()

if __name__ == "__main__":
    main()
"""