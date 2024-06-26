# Postit

Postit is a Django-based web application for creating and managing posts, for those who are wanting to share their services online. Users can create, edit, delete their posts, and view everyones posts.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Features
- User authentication (registration, login, logout)
- Create, read, update, and delete (CRUD) operations for posts
- Responsive design

## Installation

### Prerequisites
- Python 3.x
- Django 3.x or higher
- Git

### Setup

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/postit.git
    cd postit
    ```

2. **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run migrations:**
    ```bash
    python manage.py migrate
    ```

5. **Create a superuser:**
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

7. Open your browser and go to `http://127.0.0.1:8000/` to see the application in action.

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
- **Database:** Default is SQLite. For production, configure the database settings in `postit/settings.py`.
- **Static files:** Collect static files using `python manage.py collectstatic`.

## Thank you


