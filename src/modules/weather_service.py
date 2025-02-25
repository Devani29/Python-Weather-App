import requests
import pytz
import logging
from tkinter import *
from tkinter import messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
from config.environment_variable import api_key

logger = logging.getLogger(__name__)

def fetch_weather(city, country_code, zip_code):
    """Fetch weather data from Openweather API."""
    logger.info(f"Fetching weather data for {city}, {country_code}, {zip_code}...")

    if zip_code:
        url = f"http://api.openweathermap.org/data/2.5/weather?zip={zip_code},{country_code}&appid={api_key}&units=metric&lan=en"
    elif city:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&appid={api_key}&units=metric&lang=en"
    else:
        messagebox.showerror("Error", "Please enter a valid city or ZIP code.")
        return None
    
    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            return data
        else:
            logger.info(data)
            messagebox.showerror("Error", "City or ZIP code not found!")
            return None
    except requests.exception.RequestException:
        messagebox.showerror("Error", "There's a problem with the API connection!")
    

def extract_weather_data(data):
    """Extract relevant weather details from API response."""
    if not data:
        return None
    
    lat, lon = data["coord"]["lat"], data["coord"]["lon"]
    obj = TimezoneFinder()
    result = obj.timezone_at(lng=lon, lat=lat)

    home = pytz.timezone(result)
    local_time = datetime.now(home).strftime("%I:%M:%p")

    return {
        "city_name": data["name"],
        "description": data['weather'][0]['description'],
        "temp": round(data['main']['temp']),
        "temp_min": round(data['main']['temp_min']),
        "temp_max": round(data['main']['temp_max']),
        "feels_like": round(data['main']['feels_like']),
        "pressure": data['main']['pressure'],
        "humidity": data['main']['humidity'],
        "wind": data["wind"]['speed'],
        "local_time": local_time,
    }

    
