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
            # geolocator=Nominatim(user_agent="weather_app")
            lat = data["coord"]["lat"]
            lon = data["coord"]["lon"]
            # location=geolocator.geocode(city)
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
def on_focus_in_city(event):
    if entry_city.get() == "City":
        entry_city.delete(0, tk.END)
        entry_city.config(fg="white")

def on_focus_out_city(event):
    if entry_city.get() == "":
        entry_city.insert(0, "City")
        entry_city.config(fg="gray")

def on_focus_in_country(event):
    if entry_country_code.get() == "Country Code (mx,us)":
        entry_country_code.delete(0, tk.END)
        entry_country_code.config(fg="white")

def on_focus_out_country(event):
    if entry_country_code.get() == "":
        entry_country_code.insert(0, "Country Code (mx,us)")
        entry_country_code.config(fg="gray")

def on_focus_in_zip(event):
    if entry_zip_code.get() == "ZIP Code":
        entry_zip_code.delete(0, tk.END)
        entry_zip_code.config(fg="white")

def on_focus_out_zip(event):
    if entry_zip_code.get() == "":
        entry_zip_code.insert(0, "ZIP Code")
        entry_zip_code.config(fg="gray")



# Show shadow
def on_enter(event):
    global shadow_white
    if shadow_white is None:
        shadow_white = my_canvas.create_image(133,196, image=shadow_white_tk, anchor="nw")
        my_canvas.tag_lower(shadow_white, button)  

# Hide shadow
def on_leave(event):
    global shadow_white
    if shadow_white:
        my_canvas.delete(shadow_white)
        shadow_white = None

def on_click(event):
    global shadow_black
    if shadow_black is None:
        shadow_black = my_canvas.create_image(133,196, image=shadow_black_tk, anchor="nw")
        my_canvas.tag_lower(shadow_black, button)
    print("click")

def on_release(event):
    global shadow_black
    if shadow_black:
        my_canvas.delete(shadow_black)
        shadow_black = None
    print("release")
    weather_app()
    


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
shadow_white_img = Image.new("RGBA", (50,50),(255,255,255,100))
draw_white = ImageDraw.Draw(shadow_white_img)
draw_white.rectangle([0,0,49,49], outline=(255,255,255,100), width=3)
shadow_white_tk = ImageTk.PhotoImage(shadow_white_img)

# Black shadows
shadow_black_img = Image.new("RGBA", (50, 50), (0, 0, 0, 100)) 
draw_black = ImageDraw.Draw(shadow_black_img)
draw_black.rectangle([0, 0, 49, 49], outline=(0, 0, 0, 180), width=1)
shadow_black_tk = ImageTk.PhotoImage(shadow_black_img)

# Save references 
root.shadow_black_tk = shadow_black_tk
root.shadow_white_tk = shadow_white_tk

# Shadow variables
shadow_black = None
shadow_white = None

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
entry_city=tk.Entry(root, justify="center", width=21, font=("poppins",16,"bold"), bg="#23333d", border=0, fg="gray", highlightthickness=0, insertbackground="black")
entry_city.insert(0, "City")
entry_window=my_canvas.create_window(35,38, window=entry_city, anchor="nw")

entry_city.bind("<FocusIn>", on_focus_in_city)
entry_city.bind("<FocusOut>", on_focus_out_city)

entry_country_code=tk.Entry(root, justify="center", width=21, font=("poppins",16,"bold"), bg="#202e3b", border=0, fg="gray", highlightthickness=0, insertbackground="black")
entry_country_code.insert(0, "Country Code (mx,us)")
entry_window2=my_canvas.create_window(35,98, window=entry_country_code, anchor="nw")

entry_country_code.bind("<FocusIn>", on_focus_in_country)
entry_country_code.bind("<FocusOut>", on_focus_out_country)

entry_zip_code=tk.Entry(root, justify="center", width=21, font=("poppins",16,"bold"), bg="#1d2b37", border=0, fg="gray", highlightthickness=0, insertbackground="black")
entry_zip_code.insert(0, "ZIP Code")
entry_window3=my_canvas.create_window(35,158, window=entry_zip_code, anchor="nw")

entry_zip_code.bind("<FocusIn>", on_focus_in_zip)
entry_zip_code.bind("<FocusOut>", on_focus_out_zip)


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
my_canvas.tag_bind(button, "<Enter>", on_enter)
my_canvas.tag_bind(button, "<Leave>", on_leave)
my_canvas.tag_bind(button, "<ButtonPress-1>", on_click)
my_canvas.tag_bind(button, "<ButtonRelease-1>", on_release)


root.mainloop()