## Overview
`test.py` contains test cases for verifying the API's functionality using Pytest and FastAPI's `TestClient`. It ensures that the application behaves as expected by running isolated unit tests.

## Key Components
1. **TestClient**
   - Simulates API requests and checks responses.

2. **Database Session Override**
   - Uses `app.dependency_overrides` to inject a test database session, preventing tests from modifying production data.

3. **Pytest-Based Test Cases**
   - Includes test functions for CRUD operations.

## How It Works
1. A test client sends HTTP requests to the FastAPI app.
2. The overridden dependency provides a temporary test session.
3. Assertions validate the expected API behavior.

## Running Tests
Run all tests using:
```sh
pytest test.py
```