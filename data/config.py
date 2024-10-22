from dotenv import load_dotenv
import os

load_dotenv()

LOGIN = str(os.getenv("LOGIN"))
PASSWORD = str(os.getenv("PASSWORD"))
URL = str(os.getenv("URL"))

