from dotenv import load_dotenv
import os

load_dotenv()

LOGIN = str(os.getenv("LOGIN"))
PASSWORD = str(os.getenv("PASSWORD"))
URL_AUTH = str(os.getenv("URL_AUTH"))
URL_API = str(os.getenv("URL_API"))