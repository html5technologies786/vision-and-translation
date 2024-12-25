import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GROQCLOUD_API_KEY")

if api_key:
    print("API Key Loaded Successfully:", api_key)
else:
    print("Failed to load API Key. Check .env file.")
