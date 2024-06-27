# PostIt

PostIt is a Django-based web application for creating and managing posts, for those who are wanting to share their services online in South Africa. Users can create, edit, delete their own posts, and view everyones posts.

Project state -> In Development.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [License](#license)

## Features
- Create, read, update, and delete (CRUD) operations for JobPosts

## Installation

### Prerequisites
- Python 3.x
- Django 3.x or higher
- Postgres (@14 or higher)
- Git

### Setup

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/postit.git
    cd postit
    ```
2. **Create a database
    ```bash

    CREATE DATABASE database;

    CREATE USER database WITH PASSWORD '';

    ALTER ROLE database SET default_transaction_isolation TO 'read committed';

    ALTER ROLE database SET timezone TO 'UTC';

    ALTER DATABASE database OWNER TO databaseowner;
    ```

3. **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

4. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

5. **Run migrations:**
    ```bash
    python manage.py migrate
    ```

6. **Create a superuser:**
    ```bash
    python manage.py createsuperuser
    ```

7. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

8. Open your browser and go to `http://127.0.0.1:8000/` to see the application in action.

## Usage

### Creating a Post
1. Log in to the application.
2. Navigate to the "Create Post" page.
3. Fill out the form and submit.

### Editing a Post
1. Navigate to the post you want to edit.
2. Click the "Edit" button.
3. Make your changes and submit.

### Deleting a Post
1. Navigate to the post you want to delete.
2. Click the "Delete" button.

## Configuration
- **Database:** Default is PostgreSQL. For production, configure the database settings in `postit/settings.py`.
- **Static files:** Collect static files using `python manage.py collectstatic`.

## Feel free to contribute and open PR's :

Ideation board <br/> 
https://www.figma.com/board/Jb9WCXvCkIHV0mGRlaqA96/PostIt---Ideation-Space?node-id=0-1&t=s4LQHB0vwWZCUu8w-0 


