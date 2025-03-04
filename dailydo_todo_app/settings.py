import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the DATABASE_URL environment variable
DATABASE_URL = os.getenv("DATABASE_URL")
TEST_DATABASE_URL = os.getenv("TEST_DATABASE_URL")

# If you need to keep it secret, you can handle it like this:
class Secret(str):
    def __repr__(self):
        return "******"  # Hide the actual secret when printed

DATABASE_URL = Secret(DATABASE_URL) if DATABASE_URL else None
TEST_DATABASE_URL = Secret(TEST_DATABASE_URL) if TEST_DATABASE_URL else None


# from starlette.config import config
# from starlette.datastructures import Secret

# try:
#     config = Config(".env")

# except FileNotFoundError:
#     config = Config()

# DATABASE_URL = config("DATABASE_URL", cast = Secret)

