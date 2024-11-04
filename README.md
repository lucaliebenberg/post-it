# Post It

PostIt is a Django-based web application for creating and managing posts, aimed at helping those who hand out job slips at traffic robots in South Africa by providing a self-service platform to share their slips. Users can create, edit, delete their own posts, and view everyone's posts.

Project state -> In Product Development.

## Installation

### Prerequisites
- Python 3.x
```sh
python --version
# or
python3 --version

```
- Django 3.x or higher
```
django --version
```
- Postgres (@14 or higher)
```
postgres --version
```
- Git

### Setup

Mac/Linux

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/postit.git
    cd postit
    ```
2. **Create a PostgreSQL database:**
    ```bash
    psql

    CREATE DATABASE postit_db;

    CREATE postit_user database WITH PASSWORD 'yourpassword';

    ALTER ROLE postit_user SET default_transaction_isolation TO 'read committed';

    ALTER ROLE postit_user SET timezone TO 'UTC';

    ALTER DATABASE postit_db OWNER TO postit_user;
    ```

3. **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  
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


Windows

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/postit.git
    cd postit
    ```
2. **Create a PostgreSQL database:**
    ```bash
    psql

    CREATE DATABASE postit_db;

    CREATE postit_user database WITH PASSWORD 'yourpassword';

    ALTER ROLE postit_user SET default_transaction_isolation TO 'read committed';

    ALTER ROLE postit_user SET timezone TO 'UTC';

    ALTER DATABASE postit_db OWNER TO postit_user;
    ```

3. **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv\Scripts\activate  
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


### Installing Django, Pip, and PostgreSQL

#### Mac/Linux

1. **Install Python:**
    - Download and install Python from [python.org](https://www.python.org/downloads/).

2. **Install Pip:**
    - Pip comes pre-installed with Python 3.4 and later. To upgrade Pip, run:
    ```sh
    python -m pip install --upgrade pip
    ```

3. **Install Django:**
    ```sh
    pip install django
    ```

4. **Install PostgreSQL:**
    - For macOS, you can use Homebrew:
    ```sh
    brew install postgresql
    brew services start postgresql
    ```

    - For Linux, use your package manager:
    ```sh
    sudo apt-get update
    sudo apt-get install postgresql postgresql-contrib
    ```

#### Windows

1. **Install Python:**
    - Download and install Python from [python.org](https://www.python.org/downloads/). Ensure you check the box to add Python to your PATH during installation.

2. **Install Pip:**
    - Pip comes pre-installed with Python 3.4 and later. To upgrade Pip, run:
    ```sh
    python -m pip install --upgrade pip
    ```

3. **Install Django:**
    ```sh
    pip install django
    ```

4. **Install PostgreSQL:**
    - Download and install PostgreSQL from [postgresql.org](https://www.postgresql.org/download/windows/). During installation, you can set the password for the PostgreSQL superuser (postgres) and choose the components you want to install. Ensure that "pgAdmin 4" is selected.
    - After installation, start the PostgreSQL service using `pgAdmin 4` or the PostgreSQL shell.

## Configuration
- **Database:** Default is PostgreSQL. For production, configure the database settings in `postit/settings.py`.
- **Static files:** Collect static files using `python manage.py collectstatic`.

## Feel free to contribute and open PR's
