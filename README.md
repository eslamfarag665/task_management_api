# Task Management API

This project is a Task Management API built with Django and Django REST Framework. It includes user authentication functionality and task management features.

## Setup

1. Clone the repository
2. Create a virtual environment and activate it
3. Install the required packages:
   ```
   pip install django djangorestframework django-filter
   ```
4. Run migrations:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```
5. Start the development server:
   ```
   python manage.py runserver
   ```

## User Model

The project uses a custom user model (`CustomUser`) that extends Django's `AbstractUser`. It includes the following fields:

- Username
- Email (unique)
- Password

Additional fields can be added to the `CustomUser` model in `accounts/models.py` as needed.

## API Endpoints

### User Authentication
- User Registration: POST `/api/accounts/register/`
- User Login: POST `/api/accounts/login/`
- User Logout: POST `/api/accounts/logout/`

### Task Model
The Task model includes the following fields:

- title: CharField
- description: TextField
- due_date: DateField
- priority_level: CharField (choices: LOW, MEDIUM, HIGH)
- status: CharField (choices: PENDING, COMPLETED)
- user: ForeignKey to User model

### Task Management
- List/Create Tasks: GET/POST `/api/tasks/`
- Retrieve/Update/Delete Task: GET/PUT/DELETE `/api/tasks/<task_id>/`

#### Filtering and Sorting
- Filter tasks: GET `/api/tasks/?status=PENDING&priority_level=HIGH`
- Sort tasks: GET `/api/tasks/?ordering=-due_date`

## Authentication

The API uses Token Authentication. Include the token in the Authorization header for protected endpoints:

```
Authorization: Token <your-token-here>
```

## Task Endpoints

### Create a Task
**URL**: `/api/tasks/`  
**Method**: `POST`  
**Authentication**: Required  
**Request Body**:  
```json
{
    "title": "Task title",
    "description": "Task description",
    "due_date": "YYYY-MM-DD",
    "priority_level": "High",
    "status": "Pending"
}

