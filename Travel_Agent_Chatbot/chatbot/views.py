#from django.http import HttpResponse

#def index(request):
    #return HttpResponse("Hello from the root path!")

# chatbot/views.py

import json
import openai
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .extract_user_intent import interpret_user_intent
from .models import City, Distance, FlightTime, TravelPackage, TravelAgent

# Setting OpenAI API key
openai.api_key = 'jhalak_surve'

@csrf_exempt
def handle_user_query(request):
    data = json.loads(request.body)
    user_message = data['message']

    # Using NLP to interpret user intent
    user_intent = interpret_user_intent(user_message)

    # Check if user is asking about travel-related queries
    if user_intent.get('intent') == 'travel_package':
        return handle_travel_related_queries(user_message, user_intent)

    # If no specific intent is detected, use ChatGPT or provide a default response
    response_message = generate_chatgpt_response(user_message)
    return JsonResponse({'message': response_message})

def handle_travel_related_queries(user_message, user_intent):

    # Check if the user is asking about travel packages, travel agents, or costs
    if user_intent.get('intent') == 'travel_package':
        return handle_travel_package_query(user_intent)
    elif user_intent.get('intent') == 'travel_agent':
        return handle_travel_agent_query(user_intent)
    elif user_intent.get('intent') == 'cost_query':
        return handle_cost_query(user_intent)

    # If no specific travel-related intent is detected, use ChatGPT or provide a default response
    response_message = generate_chatgpt_response(user_message)
    return JsonResponse({'message': response_message})

def handle_travel_package_query(user_intent):
    # Use NL SQL or any other logic to query the travel package information
    destination = user_intent.get('destination')
    travel_agent = user_intent.get('travel_agent')

    # Query the database for travel package information
    try:
        travel_package = TravelPackage.objects.get(destination=destination, travel_agent=travel_agent)
        response_message = f"The travel package to {destination} with {travel_agent} includes {travel_package.details}."
    except TravelPackage.DoesNotExist:
        response_message = f"Sorry, we couldn't find information about the travel package to {destination} with {travel_agent}."

    return JsonResponse({'message': response_message})

def handle_travel_agent_query(user_intent):
    # Use NL SQL or any other logic to query information about the travel agent
    travel_agent = user_intent.get('travel_agent')

    # Query the database for information about the travel agent
    try:
        agent_details = TravelAgent.objects.get(name=travel_agent).details
        response_message = f"{travel_agent} is a travel agent. {agent_details}"
    except TravelAgent.DoesNotExist:
        response_message = f"Sorry, we couldn't find information about the travel agent {travel_agent}."

    return JsonResponse({'message': response_message})

def handle_cost_query(user_intent):
    # Using NL SQL or any other logic to query the cost information
    destination = user_intent.get('destination')

    # Querying the database for cost information
    try:
        # Modify the following line based on your database structure
        travel_package = TravelPackage.objects.filter(destination=destination).first()
        
        if travel_package:
            response_message = f"The cost for {destination} is {travel_package.cost}."
        else:
            response_message = f"Sorry, we couldn't find cost information for {destination}."
    except Exception as e:
        print(f"Error handling cost query: {e}")
        response_message = "Sorry, there was an error processing your cost query."

    return JsonResponse({'message': response_message})

def generate_chatgpt_response(user_message):
    # Making a request to the OpenAI GPT API to get a response
    try:
        response = openai.Completion.create(
            engine="text-davinci-002",  
            prompt=user_message,
            max_tokens=150,
            n=1,
            stop=None
        )
        chatgpt_response = response.choices[0].text.strip()
    except Exception as e:
        print(f"Error generating ChatGPT response: {e}")
        chatgpt_response = "Sorry, there was an error processing your request."

    return chatgpt_response


"""# chatbot/views.py

import json
import openai
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from .extract_user_intent import interpret_user_intent
from .models import City, Distance, FlightTime, TravelPackage, TravelAgent

# Setting OpenAI API key
openai.api_key = 'jhalak_surve'

@api_view(['POST'])
@permission_classes([AllowAny])
class HandleUserQueryView(APIView):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        user_message = data['message']

        # Using NLP to interpret user intent
        user_intent = interpret_user_intent(user_message)

        # Check if user is asking about travel-related queries
        if user_intent.get('intent') == 'travel_package':
            return self.handle_travel_related_queries(user_intent,user_message)

        # If no specific intent is detected, use ChatGPT or provide a default response
        response_message = self.generate_chatgpt_response(user_message)
        return Response({'message': response_message})

    def handle_travel_related_queries(self, user_intent, user_message):
        # Check if the user is asking about travel packages, travel agents, or costs
        if user_intent.get('intent') == 'travel_package':
            return self.handle_travel_package_query(user_intent)
        elif user_intent.get('intent') == 'travel_agent':
            return self.handle_travel_agent_query(user_intent)
        elif user_intent.get('intent') == 'cost_query':
            return self.handle_cost_query(user_intent)

        # If no specific travel-related intent is detected, use ChatGPT or provide a default response
        response_message = self.generate_chatgpt_response(user_message)
        return Response({'message': response_message})

    def handle_travel_package_query(self, user_intent):
        # Use NL SQL or any other logic to query the travel package information
        destination = user_intent.get('destination')
        travel_agent = user_intent.get('travel_agent')

        # Query the database for travel package information
        try:
            travel_package = TravelPackage.objects.get(destination=destination, travel_agent=travel_agent)
            response_message = f"The travel package to {destination} with {travel_agent} includes {travel_package.details}."
        except TravelPackage.DoesNotExist:
            response_message = f"Sorry, we couldn't find information about the travel package to {destination} with {travel_agent}."

        return Response({'message': response_message})

    def handle_travel_agent_query(self, user_intent):
        # Use NL SQL or any other logic to query information about the travel agent
        travel_agent = user_intent.get('travel_agent')

        # Query the database for information about the travel agent
        try:
            agent_details = TravelAgent.objects.get(name=travel_agent).details
            response_message = f"{travel_agent} is a travel agent. {agent_details}"
        except TravelAgent.DoesNotExist:
            response_message = f"Sorry, we couldn't find information about the travel agent {travel_agent}."

        return Response({'message': response_message})

    def handle_cost_query(self, user_intent):
        # Use NL SQL or any other logic to query the cost information
        destination = user_intent.get('destination')
        # You might have additional parameters for cost queries
    

    # Querying the database for cost information
        try:
        # Modify the following line based on your database structure
            travel_package = TravelPackage.objects.filter(destination=destination).first()
        
            if travel_package:
                response_message = f"The cost for {destination} is {travel_package.cost}."
            else:
                response_message = f"Sorry, we couldn't find cost information for {destination}."
        except Exception as e:
            print(f"Error handling cost query: {e}")
        response_message = "Sorry, there was an error processing your cost query."

    
        return Response({'message': response_message})

    def generate_chatgpt_response(self, user_message):
        # Make a request to the OpenAI GPT API to get a response
        try:
            response = openai.Completion.create(
                engine="text-davinci-002",  # You can experiment with different engines
                prompt=user_message,
                max_tokens=150,
                n=1,
                stop=None
            )
            chatgpt_response = response.choices[0].text.strip()
        except Exception as e:
            print(f"Error generating ChatGPT response: {e}")
            chatgpt_response = "Sorry, there was an error processing your request."

        return Response({'message': chatgpt_response})
"""
