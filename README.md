# Travel Chatbot using Django, ChatGPT and NL-SQL

Welcome to the Travel Chatbot project! This is a smart chatbot designed to assist users with various travel-related queries. Leveraging the power of Django for the backend and integrating seamlessly with OpenAI's ChatGPT, the chatbot provides an intelligent and interactive experience for users seeking information about travel packages, travel agents, and associated costs.

## Technology Stack

- **Django:** A high-level Python web framework for building robust web applications.
- **ChatGPT:** OpenAI's language model for natural language processing and intelligent responses.
- **NL SQL:** Utilizes Natural Language Structured Query Language for user-friendly database queries.

## Features

- **Handle User Queries**: Process user queries related to travel, interpret intents, and provide relevant information.
- **ChatGPT Integration**: Utilize the ChatGPT API for generating responses to user messages.
- **Travel Database**: Store information about cities, distances, flight times, travel packages, and travel agents.
- **React Frontend**: Create a user-friendly chat interface using React.

## Project Structure

- `chatbot/`: Django app containing backend logic and API endpoints.
- `frontend/`: React application for the chatbot frontend.
- `extract_user_intent.py`: Module for interpreting user intents from messages.
- `models.py`: Define Django models for the travel-related database.
- `OpenAI API`: Set OpenAI API key for ChatGPT.

## Setup

1. **Clone the repository:**
    git clone https://github.com/jhalak1509/Travel_Chatbot_Using_Chatgpt.git

2. **Navigate to the project directory:**
    cd Travel_Agent_Chatbot

3. **Create a virtual environment:**
    python -m venv venv

4. **Activate the virtual environment:**
    - On Windows:
        .\venv\Scripts\activate

    - On Unix or MacOS:
        source venv/bin/activate

5. **Install the required dependencies:**
    pip install -r requirements.txt
  

## Database Setup

1. **Apply migrations to set up the database:**
    python manage.py migrate

2. **(Optional) Load initial data or create a superuser for the Django admin:**
    python manage.py loaddata initial_data
    # or
    python manage.py createsuperuser

## Run the Development Server

Start the Django development server:
python manage.py runserver

Access the application at http://localhost:8000
