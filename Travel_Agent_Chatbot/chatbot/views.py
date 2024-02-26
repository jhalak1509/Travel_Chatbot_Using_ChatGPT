# Travel_Agent_Chatbot/views.py

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello from the root path!")
