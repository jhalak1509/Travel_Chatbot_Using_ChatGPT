# Travel Chatbot using Django, ChatGPT and NL-SQL

Welcome to the Travel Chatbot project! This is a smart chatbot designed to provide users with an interactive platform to explore travel packages, destinations, and costs.

<img width="497" alt="image" src="https://github.com/jhalak1509/Travel_Chatbot_Using_ChatGPT/assets/114832299/5e3f8f45-dd5b-4e64-8486-1cc3ea4b6852">


## Technology Stack

- **Django:** A high-level Python web framework for building robust web applications.
- **GPT-3.5:** OpenAI's language model for natural language processing and intelligent responses.
- **NL SQL:** Utilizes Natural Language Structured Query Language for user-friendly database queries.

## Features

- **Handle User Queries**: Enables dynamic data retrieval and response generation for travel-related inquiries.
- **GPT-3.5 Integration**: Integrated GPT-3.5 model to process natural language queries, converting them into SQL queries for database interaction.
- **Travel Database**: Store information about cities, distances, flight times, travel packages, and travel agents.
- **React Frontend**: Create a user-friendly chat interface using React.

## Project Structure

- `chatbot/`: Django app containing backend logic and API endpoints.
- `frontend/`: React application for the chatbot frontend.
- `models.py`: Define Django models for the travel-related database.
- `OpenAI API`: Set OpenAI API key for ChatGPT.

## Database 

<img width="1440" alt="Screen Shot 2024-05-16 at 12 32 07 PM" src="https://github.com/jhalak1509/Travel_Chatbot_Using_ChatGPT/assets/114832299/3325f1ad-a7c3-4c0a-8d08-f84c8e4cd44c">

<img width="1440" alt="Screen Shot 2024-05-16 at 12 33 08 PM" src="https://github.com/jhalak1509/Travel_Chatbot_Using_ChatGPT/assets/114832299/94938dae-cc7c-488e-8b39-0558fadd332b">

<img width="1440" alt="Screen Shot 2024-05-16 at 12 33 21 PM" src="https://github.com/jhalak1509/Travel_Chatbot_Using_ChatGPT/assets/114832299/aba6ac39-2de2-4384-b041-d5578b637137">


1. Database Setup:
    * Utilized MySQL database with SQLAlchemy ORM for storing travel-related data such as travel agents, packages, cities, airports, and flights.
    * Defined database models for TravelAgent, TravelPackage, City, Airport, and Flight in models.py.
    * Install MySQL and create a database named chatbot.
    * Update the database connection URL in database.py with your MySQL credentials.
    * Run the following commands to set up the database schema:
      python manage.py makemigrations
      python manage.py migrate
      
2. Data Population:
    * Populate the database with sample data for testing and development purposes using the provided data population script populate_data.py.

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
  

## Run the Development Server

Start the Django development server:
python manage.py runserver

Access the application at http://localhost:8000


