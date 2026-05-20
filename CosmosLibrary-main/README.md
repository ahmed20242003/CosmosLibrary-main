# CosmosLib

CosmosLib is a library management system featuring a Django REST Framework backend and a dynamic Vanilla HTML/CSS/JS frontend.

## Prerequisites

Make sure you have [Python 3.x](https://www.python.org/downloads/) installed on your machine.

## 1. Starting the Backend Server

The backend is powered by Django and serves the REST API for the application.

1. Open a terminal and navigate to the `backend` directory:
   ```bash
   cd backend
   ```

2. (Optional but recommended) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On Mac/Linux:
   source venv/bin/activate
   ```

3. Install the required Python packages:
   ```bash
   pip install django djangorestframework django-cors-headers
   ```

4. Run the database migrations to set up the SQLite database:
   ```bash
   python manage.py migrate
   ```

5. Seed the database with default books and users (like the Admin user):
   ```bash
   python seed_books.py
   ```

6. Start the Django development server:
   ```bash
   python manage.py runserver
   ```
   *The backend will now be running at `http://127.0.0.1:8000/`.*

## 2. Starting the Frontend Website

The frontend is built with pure HTML, CSS, and JS, so it requires no build step.

1. Open a new terminal and navigate to the `frontend` directory:
   ```bash
   cd frontend
   ```

2. Start a simple local web server to serve the static files:
   ```bash
   python -m http.server 5500
   ```
   *(Alternatively, you can use the "Live Server" extension in VSCode).*

3. Open your web browser and navigate to:
   ```
   http://localhost:5500/index.html
   ```

## Default Accounts

If you ran the `seed_books.py` script, the following accounts are available for testing:

- **Admin Account**
  - Email: `admin@cosmoslib.com`
  - Password: `admin123`

- **User Account**
  - Email: `ahmed@example.com`
  - Password: `user123`
