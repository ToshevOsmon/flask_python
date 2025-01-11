import dotenv
import os

dotenv.load_dotenv("variables/.env")

COUNTRY_API=os.getenv("COUNTRY_API")
DB_NAME=os.getenv("DB_NAME")