import dotenv
import os

print("env_vars1 file open")

dotenv.load_dotenv(".env")

print("dotenv is run")

COUNTRY_API=os.getenv("COUNTRY_API")

print("COUNTRY_API is loaded")