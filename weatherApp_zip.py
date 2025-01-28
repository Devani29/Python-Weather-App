from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
from PIL import Image, ImageTk 

root=Tk()
root.title("Banana's Weather App")
root.geometry("900x500+300+200")
root.resizable(False,False)
root.iconbitmap('icono.ico')


# Weather App
def weather_app():
    city=entry_city.get()
    country_code=entry_country_code.get()
    zip_code=entry_zip_code.get()


    api_key = '43cae06a72b79475dd2b698e3748854d'
    url = f'http://api.openweathermap.org/data/2.5/weather?zip={zip_code},{country_code}&q={city}&appid={api_key}&units=metric&lang=en'

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:

            geolocator=Nominatim(user_agent="weather_app")
            location=geolocator.geocode(city)
            obj=TimezoneFinder()
            result=obj.timezone_at(lng=location.longitude,lat=location.latitude)
            print(result)

            home=pytz.timezone(result)
            local_time=datetime.now(home)
            current_time=local_time.strftime("%I:%M %p")
            clock.config(text=current_time)
            # name.config(text="CURRENT WEATHER")

            weather = data['weather'][0]['main']
            description = data['weather'][0]['description']
            temp = round(data['main']['temp'])
            temp_min = round(data['main']['temp_min'])
            temp_max = round(data['main']['temp_max'])
            feels_like=round(data['main']['feels_like'])
            pressure = data['main']['pressure']
            humidity = data['main']['humidity']
            wind = data['wind']['speed']

            t.config(text=f"{temp}°")
            tmin.config(text=f"Minimum temperature {temp_min}°")
            tmax.config(text=f"Maximum temperature {temp_max}°")
            d.config(text=f"{description} | Feels like {feels_like}°")
            
            w.config(text=f"{wind}km/h")
            h.config(text=f"{humidity}%")
            p.config(text=f"{pressure}hPa")

        else:
            messagebox.showerror("Error", "Not city found!")
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


# Loading dots
def on_focus_in_wind(event):
    if w_dots.get() == "...":
        w_dots.delete(0, tk.END)
        w_dots.config(fg="black")

def on_focus_out_wind(event):
    if w_dots.get() == w:
        w_dots.insert(0, "...")
        w_dots.config(fg="black")

def on_focus_in_humidity(event):
    if h_dots.get() == "...":
        h_dots.delete(0, tk.END)
        h_dots.config(fg="black")

def on_focus_out_humidity(event):
    if h_dots.get() == h:
        h_dots.insert(0, "...")
        h_dots.config(fg="black")



# Search box
search_image=Image.open("search.png")
resized_image=search_image.resize((290,60))
search_image=ImageTk.PhotoImage(resized_image)
myimage=Label(image=search_image)
myimage.place(x=18,y=20)

search_image2=Image.open("search.png")
resized_image=search_image2.resize((290,60))
search_image2=ImageTk.PhotoImage(resized_image)
myimage2=Label(image=search_image2)
myimage2.place(x=18,y=80)

search_image3=Image.open("search.png")
resized_image=search_image3.resize((290,60))
search_image3=ImageTk.PhotoImage(resized_image)
myimage3=Label(image=search_image2)
myimage3.place(x=18,y=140)

# Search icon
search_icon1=Image.open("search_icon1.png")
resized_icon=search_icon1.resize((40,40))
search_icon1=ImageTk.PhotoImage(resized_icon)
myicon=Label(image=search_icon1)
myicon=Button(image=search_icon1,borderwidth=3,cursor="hand2",bg="#bbbbbb",command=weather_app)
myicon.place(x=130,y=200)

# Logo
logo_image=PhotoImage(file="logo.png")
logo=Label(image=logo_image)
logo.place(x=35,y=250)

# Box
box_info=Image.open("box.png")
resized_box_info=box_info.resize((550,180))
box_info=ImageTk.PhotoImage(resized_box_info)
mybox_info=Label(image=box_info)
mybox_info.place(x=325,y=300)


# Time
name=Label(root, text="CURRENT WEATHER",font=("arial",15,"bold"))
name.place(x=340,y=40)
clock=Label(root,font=("Helvetica",20))
clock.place(x=340,y=70)


# Entries
entry_city=tk.Entry(root,justify="center",width=21,font=("poppins",16,"bold"),bg="#404040",border=0,fg="gray")
entry_city.insert(0, "City")
entry_city.place(x=35,y=42)

entry_city.bind("<FocusIn>", on_focus_in_city)
entry_city.bind("<FocusOut>", on_focus_out_city)

entry_country_code=tk.Entry(root,justify="center",width=21,font=("poppins",16,"bold"),bg="#404040",border=0,fg="gray")
entry_country_code.insert(0, "Country Code (mx,us)")
entry_country_code.place(x=35,y=102)

entry_country_code.bind("<FocusIn>", on_focus_in_country)
entry_country_code.bind("<FocusOut>", on_focus_out_country)

entry_zip_code=tk.Entry(root,justify="center",width=21,font=("poppins",16,"bold"),bg="#404040",border=0,fg="gray")
entry_zip_code.insert(0, "ZIP Code")
entry_zip_code.place(x=35,y=162)

entry_zip_code.bind("<FocusIn>", on_focus_in_zip)
entry_zip_code.bind("<FocusOut>", on_focus_out_zip)

# Focus in/out info
w_dots=Label(root,text="...",font=("arial",18,"bold"),bg="#1ab5ef")
w_dots.place(x=405,y=390)
w_dots.bind("<FocusIn>", on_focus_in_wind)
w_dots.bind("<FocusOut>", on_focus_out_wind)

h_dots=Label(root,text="...",font=("arial",18,"bold"),bg="#1ab5ef")
h_dots.place(x=560,y=390)
h_dots.bind("<FocusIn>",on_focus_in_humidity)
h_dots.bind("<FocusOut>",on_focus_out_humidity)

p_dots=Label(root,text="...",font=("arial",18,"bold"),bg="#1ab5ef")



# Labels Info
label1=Label(root,text="WIND",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label1.place(x=395,y=350)

label2=Label(root,text="HUMIDITY",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label2.place(x=530,y=350)

label4=Label(root,text="PRESSURE",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label4.place(x=700,y=350)

t=Label(font=("arial",70,"bold"),fg="#ee666d")
t.place(x=400,y=140)
tmin=Label(font=("arial",15,"bold"))
tmin.place(x=560,y=160)
tmax=Label(font=("arial",15,"bold"))
tmax.place(x=560,y=200)
d=Label(font=("arial",18,"bold"))
d.place(x=410,y=250)


w=Label(font=("arial",18,"bold"),bg="#1ab5ef")
w.place(x=380,y=390)
h=Label(font=("arial",18,"bold"),bg="#1ab5ef")
h.place(x=560,y=390)
p=Label(font=("arial",18,"bold"),bg="#1ab5ef")
p.place(x=700,y=390)





root.mainloop()