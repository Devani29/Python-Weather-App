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
from focus_events import (on_focus_in_city, on_focus_out_city,
                          on_focus_in_country, on_focus_out_country,
                          on_focus_in_zip, on_focus_out_zip)
from focus_events import entry_fields
from button_events import on_enter, on_leave, on_click, on_release, create_shadows
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


# User entry

# Show shadow

# Hide shadow

# Define background
weather_bg = Image.open("assets/images/bg_weather.jpg").resize((900, 500))
weather_bg_tk = ImageTk.PhotoImage(weather_bg)

# Create a canvas
my_canvas = Canvas(root, width=900, height=500, highlightthickness=0)
my_canvas.pack(fill="both", expand=True)

# Set image in canvas
my_canvas.create_image(0,0, image=weather_bg_tk, anchor="nw")

# Time
clock=my_canvas.create_text(390,70, text="00:00", font=("Helvetica",20))
name=my_canvas.create_text(430,40, text="CURRENT WEATHER", font=("arial",15,"bold"))
name_city=my_canvas.create_text(600, 100, text="", font=("arial", 18, "bold"))

# Search box
search_image=Image.open("assets/images/search.png").resize((290,60))
search_image_tk=ImageTk.PhotoImage(search_image)
my_canvas.create_image(18,20, image=search_image_tk, anchor="nw")

search_image2=Image.open("assets/images/search.png").resize((290,60))
search_image2_tk=ImageTk.PhotoImage(search_image2)
my_canvas.create_image(18,80, image=search_image2_tk, anchor="nw")

search_image3=Image.open("assets/images/search.png").resize((290,60))
search_image3_tk=ImageTk.PhotoImage(search_image3)
my_canvas.create_image(18,140, image=search_image3_tk, anchor="nw")

# Search icon
search_icon=Image.open("assets/images/search_icon.png").resize((40,40))
search_icon_tk=ImageTk.PhotoImage(search_icon)

my_canvas.create_image(138,200, image=search_icon_tk, anchor="nw")
button=my_canvas.create_image(138,200, image=search_icon_tk, anchor="nw")

# White shadow

# Black shadows

# Save references 
# Shadow variables
shadow_refs = create_shadows(root)
root.shadow_white_tk = shadow_refs["shadow_white_tk"]
root.shadow_black_tk = shadow_refs["shadow_black_tk"]

# Box
box_info=Image.open("assets/images/box.png").resize((550,180))
box_info_data=box_info.getdata()
new_data=[(r,g,b, int(a * 0.25)) for r,g,b, a in box_info_data]
box_info.putdata(new_data)
box_info_tk=ImageTk.PhotoImage(box_info)
my_canvas.create_image(325,280, image=box_info_tk, anchor="nw")

# Logo
logo=Image.open("assets/images/logo.png")
logo_tk=ImageTk.PhotoImage(logo)
my_canvas.create_image(35,250, image=logo_tk, anchor="nw")

# Entries
entry_city, entry_country_code, entry_zip_code = entry_fields(root, my_canvas)

# Labels Info
label_wind=my_canvas.create_text(420, 345, text="WIND", font=("Helvetica",15,'bold'), fill="white")
label_hum=my_canvas.create_text(580, 345, text="HUMIDITY", font=("Helvetica",15,'bold'), fill="white")
label_pre=my_canvas.create_text(760, 345, text="PRESSURE", font=("Helvetica",15,'bold'), fill="white")


t=my_canvas.create_text(470, 170, text="", font=("arial",70,"bold"), fill="#ec3d46")
tmin=my_canvas.create_text(680, 154, text="", font=("arial",15,"bold"))
tmax=my_canvas.create_text(682, 186, text="", font=("arial",15,"bold"))
d=my_canvas.create_text(600, 250, text="", font=("arial",18,"bold"))


# Labels 
w=my_canvas.create_text(418, 395, text="---", font=("arial",18,"bold"))
h=my_canvas.create_text(580, 395, text="---", font=("arial",18,"bold"))
p=my_canvas.create_text(760, 395, text="---", font=("arial",18,"bold"))


# Enlazar eventos
my_canvas.tag_bind(button, "<Enter>", lambda event: on_enter(event, my_canvas, root.shadow_white_tk, button))
my_canvas.tag_bind(button, "<Leave>", lambda event: on_leave(event, my_canvas))
my_canvas.tag_bind(button, "<ButtonPress-1>", lambda event: on_click(event, my_canvas, root.shadow_black_tk, button))
my_canvas.tag_bind(button, "<ButtonRelease-1>", lambda event: on_release(event, my_canvas, weather_app))


root.mainloop()