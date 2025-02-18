from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENWEATHER_API_KEY")
if not api_key:
    raise ValueError("API key not found! Please set the OPENWEATHER_API_KEY environment variable.")

# print("API_KEY:", api_key)
