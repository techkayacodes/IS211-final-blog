Flask Blog Application
Description

This Flask blog application allows users to manage their own blog with functionalities including creating, editing, and deleting posts. The application features a user authentication system, with a special root admin account for administrative access.
Setup and Installation
Prerequisites

    Python 3
    Flask
    Flask-SQLAlchemy

Installation Steps

    Clone the repository to your local machine.
    Navigate to the project directory.
    Install the required dependencies:

pip install -r requirements.txt

Initialize the database:

flask db upgrade

Run the application:

arduino

    python run.py

Usage
Accessing the Application

    The application can be accessed at http://localhost:5000 after starting the server.

Root Admin Account

To access administrative functionalities, log in using the root admin account:

    Username: pythonadmin
    Password: pythonP@ss!

Features

    Create, edit, and delete blog posts.
    User authentication system.
    Special administrative privileges for the root admin account.

Contributing

Contributions to this project are welcome. Please ensure to update tests as appropriate.



**Key Components**

run.py: This is the entry point of your application. It will import the app and run it.

app/: This directory contains your application.

__init__.py: Initializes your application and brings together various components.
models.py: Contains your database models (User, Post, Category, etc.).
routes.py: All the routes for your application (e.g., home, dashboard, add_post, etc.).
auth.py: Handles authentication-related routes and logic.
templates/: Contains your HTML templates.
static/: Contains static files like CSS, JS, and images.
instance/: This directory holds instance-specific files, like the local configuration file that should not be committed to version control.

migrations/: If you use a database migration tool like Alembic, this directory will contain migration scripts.

config.py: Contains configuration variables that should not be instance-specific.

requirements.txt: Lists all Python dependencies for your application, making it easy to replicate the environment.

.gitignore: Specifies files that should not be committed to your Git repository (like venv/, instance/, etc.).

