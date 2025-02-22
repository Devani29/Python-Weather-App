import tkinter as tk
import requests
import pytz
import os
import sys
import logging
from tkinter import *
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
from PIL import Image, ImageTk, ImageDraw
from config.environment_variable import api_key
from utils.log import logging_config
from modules.focus_events import (on_focus_in_city, on_focus_out_city,
                          on_focus_in_country, on_focus_out_country,
                          on_focus_in_zip, on_focus_out_zip)
from modules.focus_events import entry_fields
from modules.button_events import on_enter, on_leave, on_click, on_release, create_shadows
from modules.ui_elements import create_ui_elements
from modules.labels_elements import create_labels
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


root=tk.Tk()
root.title("Banana's Weather App")
root.geometry("900x500+300+200")
root.resizable(False,False)
root.iconbitmap('assets/images/icono.ico')

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


# Weather App
def weather_app():
    city=entry_city.get().strip()
    country_code=entry_country_code.get().strip()
    zip_code=entry_zip_code.get().strip()

    
    logger.info(f"Fetching weather data for {city}, {country_code}, {zip_code}...")

    if zip_code:
        url = f'http://api.openweathermap.org/data/2.5/weather?zip={zip_code},{country_code}&appid={api_key}&units=metric&lang=en'
    elif city:
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&appid={api_key}&units=metric&lang=en'
    else:
        messagebox.showerror("Error", "Please enter a valid City or ZIP code.")

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            lat = data["coord"]["lat"]
            lon = data["coord"]["lon"]
            obj=TimezoneFinder()
            result=obj.timezone_at(lng=lon,lat=lat)

            home=pytz.timezone(result)
            local_time=datetime.now(home)
            current_time=local_time.strftime("%I:%M %p")
            my_canvas.itemconfig(clock, text=current_time)

            city_name=data["name"]
            description = data['weather'][0]['description']
            temp = round(data['main']['temp'])
            temp_min = round(data['main']['temp_min'])
            temp_max = round(data['main']['temp_max'])
            feels_like=round(data['main']['feels_like'])
            pressure = data['main']['pressure']
            humidity = data['main']['humidity']
            wind = data['wind']['speed']

            my_canvas.itemconfig(name_city, text=city_name)


            my_canvas.itemconfig(t, text=f"{temp}°")
            my_canvas.itemconfig(tmin, text=f"Minimum temperature {temp_min}°")
            my_canvas.itemconfig(tmax, text=f"Maximum temperature {temp_max}°")
            my_canvas.itemconfig(d, text=f"{description} | Feels like {feels_like}°")

            my_canvas.itemconfig(w, text=f"{wind}km/h")
            my_canvas.itemconfig(h, text=f"{humidity}%")
            my_canvas.itemconfig(p, text=f"{pressure}hPa")
        
        else:
            logger.info(response.json())
            messagebox.showerror("Error", "City or ZIP code not found!")
    except requests.exceptions.RequestException:
        messagebox.showerror("Error", "There's a problem with the API connection!")


# # Set image in canvas
my_canvas, button = create_ui_elements(root)

# Save references 
shadow_refs = create_shadows(root)
root.shadow_white_tk = shadow_refs["shadow_white_tk"]
root.shadow_black_tk = shadow_refs["shadow_black_tk"]

# Entries
entry_city, entry_country_code, entry_zip_code = entry_fields(root, my_canvas)

# # Labels Info
clock, name, name_city, t, tmin, tmax, d, label_wind, label_hum, label_pre, w, h, p = create_labels(my_canvas)

# Enlazar eventos
my_canvas.tag_bind(button, "<Enter>", lambda event: on_enter(event, my_canvas, root.shadow_white_tk, button))
my_canvas.tag_bind(button, "<Leave>", lambda event: on_leave(event, my_canvas))
my_canvas.tag_bind(button, "<ButtonPress-1>", lambda event: on_click(event, my_canvas, root.shadow_black_tk, button))
my_canvas.tag_bind(button, "<ButtonRelease-1>", lambda event: on_release(event, my_canvas, weather_app))


root.mainloop()