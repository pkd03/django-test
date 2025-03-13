# Simple CRM System

A comprehensive Customer Relationship Management (CRM) system built with Django and Django REST Framework.

## Features

- Customer Management
- Product Management
- Employee Management
- Task Board Management (similar to Trello)
- JWT Authentication
- Admin Interface
- API Documentation with Swagger

## Installation

1. Clone the repository:

git clone https://github.com/pkd03/django-test

cd crm

2. Create a virtual environment and install dependencies:
   
python -m venv venv

source venv/bin/activate  # On Windows: venv\Scripts\activate

pip install -r requirements.txt

3.Create a `.env` file in the project root and add your environment variables.

4. Apply migrations:
   
python manage.py migrate

5. Create a superuser:
   
python manage.py createsuperuser

6. Run the development server:
    
python manage.py runserver

## API Documentation

API documentation is available at `/api/schema/swagger-ui/` after running the server.

## Deployment



