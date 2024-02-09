# All That Golf

This is a REST API built with Python and FastAPI using SQLAlchemy for CRUD operations on users, courses, rounds, and scores.

## Installation

### Clone this repository to your local machine:

```bash
git clone git@github.com:mgregerson/all-that-golf.git
```

### Change into the project directory:

```bash
cd all-that-golf
```

### Install the project dependencies:

```bash
pip install -r requirements.txt
```

### Connect to a database of your choice

To connect all-that-golf to a database of your choice, you'll need to set up the database URI (Uniform Resource Identifier) in your project.

### Steps:

1. Open the `config.py` file in your project directory.

2. Look for the variable named `uri`. This variable should contain the URI for your database. If you're using a local database, the URI might look like `sqlite:///./test.db`. If you're using a remote database service like PostgreSQL, the URI might look like `postgresql://username:password@hostname:port/database_name`.

3. Replace the placeholder value in `uri` with the correct URI for your database. **Remember to keep your database uri private!**

4. Save the `config.py` file.

5. Now, your FastAPI application is configured to connect to the specified database.

### Example code snippet:

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config import uri

DATABASE_URL = uri

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
```

### Run the application:

```bash
uvicorn main:app --reload
```

The application will start and be available at `http://localhost:8000`.

## API Endpoints

### User Endpoints

#### Retrieve a list of users:

```http
GET /users
```

Returns a list of all users in the system.

#### Retrieve details for a specific user:

```http
GET /users/{user_id}
```

Returns details for a specific user with the given `user_id`.

#### Add a new user:

```http
POST /users
```

Adds a new user to the system. The request body should include a JSON object with the following properties:

- **username** (string, required): the username of the user
- **first_name** (string, required): the first name of the user
- **last_name** (string, required): the last name of the user
- **email** (string, required): the email address of the user
- **password** (string, required): the password for the user

### Course Endpoints

#### Retrieve a list of courses:

```http
GET /courses
```

Returns a list of all courses in the system.

#### Retrieve details for a specific course:

```http
GET /courses/{course_id}
```

Returns details for a specific course with the given `course_id`.

#### Add a new course:

```http
POST /courses/
```

Adds a new course to the system. The request body should include a JSON object with the following properties:

- **name** (string, required): the name of the course
- **city** (string, required): the city where the course is located
- **state** (string, required): the state where the course is located
- **par** (integer, required): the par value for the course

### Round Endpoints

#### Retrieve a list of rounds:

```http
GET /rounds
```

Returns a list of all rounds in the system.

#### Retrieve details for a specific round:

```http
GET /rounds/{round_id}
```

Returns details for a specific round with the given `round_id`.

#### Add a new round:

```http
POST /rounds/
```

Adds a new round to the system. The request body should include a JSON object with the following properties:

- **user_id** (string, required): the ID of the user associated with the round
- **course_id** (string, required): the ID of the course associated with the round
- **date** (string, required): the date of the round (format: "YYYY-MM-DD")

### Score Endpoints

#### Add scores for a round:

```http
POST /scores/{round_id}
```

Adds scores for a specific round. The request body should include a list of JSON objects, each representing a score with the following properties:

- **hole_number** (integer, required): the number of the hole
- **score** (integer, required): the score for the hole