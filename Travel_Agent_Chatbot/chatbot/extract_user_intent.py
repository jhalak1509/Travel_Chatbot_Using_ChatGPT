import spacy

# Load the spaCy English model
nlp = spacy.load("en_core_web_sm")

def interpret_user_intent(user_message):
    # Processing the user message using spaCy
    doc = nlp(user_message)
    
    # Dictionary to store interpreted user intent
    user_intent = {}

    # Extracting city names
    for ent in doc.ents:
        if ent.label_ == 'GPE':
            user_intent['city'] = ent.text

     # Identifying if user is asking about travel packages
    if 'travel package' in user_message.lower():
        user_intent['intent'] = 'travel_package'
        # Extracting travel agent and destination
        for token in doc:
            if token.dep_ == 'amod' and token.head.text == 'agent':
                user_intent['travel_agent'] = token.text
            if token.dep_ == 'pobj' and token.head.text == 'to':
                user_intent['destination'] = token.text

    # Identifying if user is asking about distance between cities
    if 'distance' in user_message.lower() and any(token.text.lower() == 'between' for token in doc):
        user_intent['intent'] = 'distance_query'
        
        # Extracting source and destination cities
        cities = [ent.text for ent in doc.ents if ent.label_ == 'GPE']
        if len(cities) == 2:
            user_intent['source_city'] = cities[0]
            user_intent['destination_city'] = cities[1]

    # Identifying if user is asking about flight time between cities
    if 'flight time' in user_message.lower() and any(token.text.lower() == 'between' for token in doc):
        user_intent['intent'] = 'flight_time_query'
        
        # Extracting source and destination cities
        cities = [ent.text for ent in doc.ents if ent.label_ == 'GPE']
        if len(cities) == 2:
            user_intent['source_city'] = cities[0]
            user_intent['destination_city'] = cities[1]

    return user_intent
