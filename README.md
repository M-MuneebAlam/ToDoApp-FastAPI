# DailyDo Todo App

## Project Overview
DailyDo is a FastAPI-based Todo application that allows users to create, retrieve, update, and delete tasks. It leverages SQLModel for database interactions and Pytest for testing, ensuring a structured and maintainable codebase.

## Tech Stack
- **FastAPI** – Web framework for building APIs
- **SQLModel** – ORM for database interactions
- **PostgreSQL** – Database for storing todo tasks
- **Pytest** – Testing framework
- **TestClient** – For API testing

## Project Structure
```
project-root/
│── dailydo_todo_app/
│   ├── __init__.py
│   ├── main.py  # Main FastAPI application, API routes, SQLModel, Database setup
│   ├── settings.py  # Configuration settings
│── test.py  # Pytest test cases
│   ├── __init__.py
│   ├── test_main.py  # Test cases for API endpoints
│── .env  # Environment variables
│── pyproject.toml  # Poetry project configuration
│── README.md  # Documentation
```

## Installation & Setup

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/dailydo-todo-app.git
   cd dailydo-todo-app
   ```

2. **Install Poetry:**
   ```sh
   curl -sSL https://install.python-poetry.org | python3 -
   ```

3. **Install dependencies:**
   ```sh
   poetry install
   ```

4. **Activate the virtual environment:**
   ```sh
   poetry shell
   ```

5. **Set up environment variables:**
   Create a `.env` file and configure it with your PostgreSQL credentials.

6. **Run the FastAPI application:**
   ```sh
   uvicorn dailydo_todo_app.main:app --reload
   ```

## Database Setup
The database connection is established using SQLModel. Tables are created automatically when the app starts if they do not already exist.

- **Engine Creation:** Defined in `main.py` using `SQLModel.metadata.create_all(engine)`.
- **Session Management:** Managed via `get_session` dependency injection.

## API Endpoints
| Method | Endpoint        | Description              |
|--------|----------------|--------------------------|
| GET    | `/`            | Welcome message         |
| GET    | `/todos`       | Retrieve all todos      |
| GET    | `/todos/{id}`  | Retrieve a single todo  |
| POST   | `/todos`       | Create a new todo       |
| PUT    | `/todos/{id}`  | Update an existing todo |
| DELETE | `/todos/{id}`  | Delete a todo           |

## Dependency Injection & Testing
The project uses **FastAPI's dependency injection** to manage database sessions efficiently. In `test.py`, `app.dependency_overrides` replaces the real session with a test session, ensuring isolation between tests and production data.

### Running Tests
Run all tests using:
```sh
pytest test.py
```

## Contribution Guide
1. Fork the repository.
2. Create a new branch for your feature.
3. Commit your changes and push to GitHub.
4. Open a pull request for review.


## License

This project is licensed under the MIT License.
