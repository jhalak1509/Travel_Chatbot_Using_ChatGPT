import spacy
from sqlalchemy.orm import sessionmaker
from .database import engine
from sqlalchemy import text
from sqlalchemy import func
from openai import OpenAI
import os
from dotenv import load_dotenv
import json


client = OpenAI(api_key="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") 

# Load the spaCy English model
"""nlp = spacy.load("en_core_web_sm")

# Intent classification model placeholder
def classify_intent(tokens):
    # Placeholder for intent classification logic
    if 'package' or 'packages' in tokens:
        return 'PACKAGE_QUERY'
    elif 'distance' in tokens or 'time' in tokens:
        return 'DISTANCE_TIME_QUERY'
    else:
        return 'GENERAL_QUERY'

# Named entity recognition (NER) function
def extract_named_entities(query):
    doc = nlp(query)
    entities = {}
    for ent in doc.ents:
        entities[ent.label_] = ent.text
    return entities

# Process the user query
def process_query(query):
    tokens = [token.text for token in nlp(query)]
    intent = classify_intent(tokens)
    named_entities = extract_named_entities(query)
    return tokens, named_entities, intent

# Generate SQL query based on intent and named entities
def generate_sql_query(intent, named_entities):
    if intent == 'PACKAGE_QUERY':
        sql_query = construct_package_query(named_entities)
    elif intent == 'DISTANCE_TIME_QUERY':
        sql_query = construct_distance_time_query(named_entities)
    else:
        sql_query = text("SELECT * FROM travel_packages")
    return sql_query

# Construct SQL query for package query
def construct_package_query(named_entities):
    # Initialize the base query
    sql_query = text("SELECT * FROM travel_packages")

    # Check if there are any named entities to filter the query
    if named_entities:
        filters = []

        # Extract relevant information from the named entities
        destination_city = named_entities.get('GPE')

        # Add filters based on the named entities
        if destination_city:
            filters.append(text("destination = :city"))

        # Construct the WHERE clause for filtering
        if filters:
            where_clause = func.concat(*filters, " AND ")
            sql_query = sql_query.where(where_clause)

    return sql_query

# Construct SQL query for distance/time query
def construct_distance_time_query(named_entities):
    sql_query = text("SELECT * FROM flights WHERE departure_city = :origin_city AND destination_city = :destination_city")
    return sql_query

# Execute SQL query and return results
def execute_sql_query(sql_query, named_entities):
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        if named_entities:
            result = session.execute(sql_query, named_entities)
        else:
            result = session.execute(sql_query)
        data = result.fetchall()
        return data
    finally:
        session.close()

# Generate response based on query results
def generate_response(user_query):
    tokens, named_entities, intent = process_query(user_query)
    print("Tokens:", tokens)
    print("Named Entities:", named_entities)
    print("Intent:", intent)
    sql_query = generate_sql_query(intent, named_entities)
    results = execute_sql_query(sql_query, named_entities)
    if intent == 'PACKAGE_QUERY':
        response = generate_package_response(results)
    elif intent == 'DISTANCE_TIME_QUERY':
        response = generate_distance_time_response(results)
    else:
        response = generate_generic_response(user_query)
    return response


# Generate package query response
def generate_package_response(results):
    if results:
        response = "Here are the available travel packages:\n"
        for package in results:
            response += f"- {package.packagename}\n\n"
    else:
        response = "Sorry, we couldn't find any travel packages matching your criteria."
    return response

# Generate distance/time query response
def generate_distance_time_response(results):
    if results:
        response = "The flight details are as follows:\n"
        for flight in results:
            response += f"- Flight from {flight.departure_airport} to {flight.arrival_airport} takes {flight.flight_duration} hours\n"
    else:
        response = "Sorry, we couldn't find any flights matching your criteria."
    return response

# Generate generic response
def generate_generic_response(user_query):
    response = generate_chatgpt_response(user_query)
    return response

# Generate response using ChatGPT
def generate_chatgpt_response(user_query):
    return "Response"
"""
def nl_to_sql(question, openai_api_key):
    
    client = OpenAI(api_key="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")
    # Initialize the OpenAI API client
    #openai.api_key = openai_api_key

    # Schema information describing the database tables
    schema_info = """
    Database Schema:
    
    1. Table: travel_agents
       Columns:
       - id (Integer, Primary Key): Unique identifier for travel agents.
       - name (String(255)): Name of the travel agent.
       - location (String(255)): Location of the travel agent.
       
    2. Table: travel_packages
       Columns:
       - id (Integer, Primary Key): Unique identifier for travel packages.
       - agent_id (Integer, Foreign Key): References id in travel_agents table.
       - packagename (String(255)): Name of the travel package.
       - description (String(400)): Description of the travel package.
       - destination (String(255)): Destination of the travel package.
       - cost (Float): Cost of the travel package.
       - origin_city_id (Integer, Foreign Key): References id in cities table.
       - destination_city_id (Integer, Foreign Key): References id in cities table.
       - valid_from (DateTime): Validity start date of the package.
       - valid_to (DateTime): Validity end date of the package.
       
    3. Table: cities
       Columns:
       - id (Integer, Primary Key): Unique identifier for cities.
       - Cityname (String(255)): Name of the city.
       - country (String(255)): Country of the city.
       - timezone (String(255)): Timezone of the city.
       
    4. Table: airports
       Columns:
       - id (Integer, Primary Key): Unique identifier for airports.
       - city_id (Integer, Foreign Key): References id in cities table.
       - Airportname (String(255)): Name of the airport.
       - iata_code (String(255), Unique): IATA code of the airport.
       
    5. Table: flights
       Columns:
       - id (Integer, Primary Key): Unique identifier for flights.
       - departure_airport_id (Integer, Foreign Key): References id in airports table.
       - arrival_airport_id (Integer, Foreign Key): References id in airports table.
       - flight_duration (Float): Duration of the flight in hours.
       - operating_airlines (String(255)): Operating airlines for the flight.
       
    """

    # Send a completion request to OpenAI's API
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
        {"role": "system", "content":f"You are a travel agent chatbot that can convert natural language queries into SQL. Given the following schema information, please provide the SQL query for the given question:{schema_info}User Question: {question}",
        }
        ]
        
    )

    # Extract the SQL query from the completion response
    response_content = completion.choices[0].message.content
    # Remove leading and trailing ```sql characters
    response_content = response_content.strip('```sql').strip()
    # Remove newline characters from the response content
    sql_query = response_content.replace('\n', ' ').strip()

    return sql_query

def execute_sql_query(sql_query):
    Session = sessionmaker(bind=engine)
    session = Session()
    
    sql_query = sql_query.replace('\n', ' ')
    result = session.execute(text(sql_query))
    results = [tuple(row) for row in result]
    return json.dumps(results, default=str)

   
    #rows = [dict(row.items()) for row in result]
    #return json.dumps(rows) 

def gk_answer(question):
    
    client = OpenAI(api_key="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")

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a travel agent."},
            {"role": "user", "content": question}
        ]
    )
    formatted_response = completion.choices[0].message.content.strip()
    return formatted_response

def format_answer(question, answer, ):
    
    client = OpenAI(api_key="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")

    # Prepare the prompt for GPT-3 to generate a user-friendly response
    prompt = f"Translate the following database answer into a detailed, user-friendly response based on the original question:\nQuestion: {question}\nAnswer from database: {answer}\nFormatted Answer:"

    print("\n\n\n")
    print(answer)
    if answer:
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an insightful assistant, skilled in transforming raw data responses into clear, understandable language."},
                {"role": "user", "content": prompt}
            ]
        )
        formatted_response = completion.choices[0].message.content.strip()
    else:
        formatted_response = "It appears that the database did not provide a specific answer to your question. Let me Look that up online.\n"
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a travel agent."},
                {"role": "user", "content": prompt}
            ]
        )
        formatted_response += completion.choices[0].message.content.strip()

    return formatted_response

def classify_intent(user_query):
    # Split the user query into tokens
    tokens = user_query.lower().split()

    # Define keywords related to database queries
    database_keywords = ['travel', 'package', 'booking', 'flight', 'location', 'city', 'airport', 'agent']

    # Check if any database keywords are present in the user query
    if any(keyword in tokens for keyword in database_keywords):
        return 'DATABASE_QUERY'
    else:
        return 'GENERAL_INQUIRY'

def extract_intents(user_query):
    intent = classify_intent(user_query)
    return intent
