from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
from PIL import Image, ImageTk, ImageDraw, ImageEnhance
from ctypes import windll

root=tk.Tk()
root.title("Banana's Weather App")
root.geometry("900x500+300+200")
root.resizable(False,False)
root.iconbitmap('icono.ico')

# # Root rounded border 
# GWL_STYLE = -16               # Modify window style -16 it's the value for the windows style in the Windows API
# WS_CAPTION = 0x00C00000       # Enables window title bar 
# WS_THICKFRAME = 0x00040000    # Enables window border, it can be use to make rounded borders

# hwnd = windll.user32.GetParent(root.winfo_id())            # Gets ID of the app main window, root is the window creared by tkinter
# style = windll.user32.GetWindowLongW(hwnd, GWL_STYLE)      # Use the hwnd window handle to get the current windoe style
# style |= WS_CAPTION | WS_THICKFRAME                        # The operator |= is used to add the WS_CAPTION(title bar) and WS_THICKFRAME(rounded border) styles
# windll.user32.SetWindowLongW(hwnd, GWL_STYLE, style)       # The window style is uptaded with the new values


# Create a canvas
my_canvas = Canvas(root, width=900, height=500, highlightthickness=0)
my_canvas.pack(fill="both", expand=True)

# Define background
weather_bg = Image.open("bg_weather.jpg").resize((900, 500))
weather_bg_tk = ImageTk.PhotoImage(weather_bg)

# Set image in canvas
my_canvas.create_image(0,0, image=weather_bg_tk, anchor="nw")

# Search box
search_image=Image.open("search.png").resize((290,60))
search_image_tk=ImageTk.PhotoImage(search_image)
my_canvas.create_image(18,20, image=search_image_tk, anchor="nw")

search_image2=Image.open("search.png").resize((290,60))
search_image2_tk=ImageTk.PhotoImage(search_image2)
my_canvas.create_image(18,80, image=search_image2_tk, anchor="nw")

search_image3=Image.open("search.png").resize((290,60))
search_image3_tk=ImageTk.PhotoImage(search_image3)
my_canvas.create_image(18,140, image=search_image3_tk, anchor="nw")

# Search icon
search_icon=Image.open("search_icon.png").resize((40,40))
search_icon_tk=ImageTk.PhotoImage(search_icon)
# button_search=Button(root, image=search_icon_tk, borderwidth=3, cursor="hand2", bg="#808080") 
# button_search_window = my_canvas.create_window(130,200, anchor="nw", window=button_search)
my_canvas.create_image(138,200, image=search_icon_tk, anchor="nw")
button=my_canvas.create_image(138,200, image=search_icon_tk, anchor="nw")

# White shadow
shadow_white_img = Image.new("RGBA", (50,50),(255,255,255,100))
draw_white = ImageDraw.Draw(shadow_white_img)
draw_white.rectangle([0,0,49,49], outline=(255,255,255,100), width=3)
shadow_white_tk = ImageTk.PhotoImage(shadow_white_img)

# Black shadows
shadow_black_img = Image.new("RGBA", (50, 50), (0, 0, 0, 100))  # Color negro con 100 de opacidad
draw_black = ImageDraw.Draw(shadow_black_img)
draw_black.rectangle([0, 0, 49, 49], outline=(0, 0, 0, 180), width=1)
shadow_black_tk = ImageTk.PhotoImage(shadow_black_img)

# Save references 
root.shadow_black_tk = shadow_black_tk
root.shadow_white_tk = shadow_white_tk

# Variable para la sombra
shadow_black = None
shadow_white = None

# Box
box_info=Image.open("box.png").resize((550,180))
box_info_data=box_info.getdata()
new_data=[(r,g,b, int(a * 0.25)) for r,g,b, a in box_info_data]
box_info.putdata(new_data)
# enhancer=ImageEnhance.Color(box_info)
# box_info_tinted=enhancer.enhance(0.7)
box_info_tk=ImageTk.PhotoImage(box_info)
my_canvas.create_image(325,300, image=box_info_tk, anchor="nw")

# Logo
logo=Image.open("logo.png")
logo_tk=ImageTk.PhotoImage(logo)
my_canvas.create_image(35,250, image=logo_tk, anchor="nw")

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
        entry_city.config(fg="black")

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

def on_focus_in_pressure(event):
    if p_dots.get() == "...":
        p_dots.delete(0,tk.END)
        p_dots.config(fg="black")

def on_focus_out_pressure(event):
    if p_dots.get() == p:
        p_dots.insert(0,"...")
        p_dots.config(fg="black")

# Función para mostrar sombra (con imagen)
def on_enter(event):
    global shadow_white
    if shadow_white is None:
        shadow_white = my_canvas.create_image(133,196, image=shadow_white_tk, anchor="nw")
        my_canvas.tag_lower(shadow_white, button)  # Mueve la sombra debajo del botón

# Función para ocultar sombra
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

def on_release(event):
    global shadow_black
    if shadow_black:
        my_canvas.delete(shadow_black)
        shadow_black = None


# Time
name=my_canvas.create_text(430,40, text="CURRENT WEATHER", font=("arial",15,"bold"))
clock=my_canvas.create_text(365,70, text="00:00", font=("Helvetica",20))

# Entries
entry_city=tk.Entry(root, justify="center", width=21, font=("poppins",16,"bold"), bg="#23333d", border=0, fg="gray", highlightthickness=0, insertbackground="black")
entry_city.insert(0, "City")
entry_window=my_canvas.create_window(35,38, window=entry_city, anchor="nw")
# entry_city.place(x=35,y=42)

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

# Focus in/out info
w_dots=Label(root,text="...",font=("arial",18,"bold"),bg="#1ab5ef")
w_dots.place(x=411,y=390)
w_dots.bind("<FocusIn>", on_focus_in_wind)
w_dots.bind("<FocusOut>", on_focus_out_wind)

h_dots=Label(root,text="...",font=("arial",18,"bold"),bg="#1ab5ef")
h_dots.place(x=565,y=390)
h_dots.bind("<FocusIn>",on_focus_in_humidity)
h_dots.bind("<FocusOut>",on_focus_out_humidity)

p_dots=Label(root,text="...",font=("arial",18,"bold"),bg="#1ab5ef")
p_dots.place(x=742,y=390)
p_dots.bind("<FocusIn>",on_focus_in_pressure)
p_dots.bind("<FocusOut>",on_focus_out_pressure)

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
p.place(x=705,y=390)

# clock_window=my_canvas.create_window(340,70,window=clock)

# def update_clock():
#     current_time=datetime.now().strftime("%I:%M %p")
#     my_canvas.itemconfig(clock, text=current_time)
#     root.after(1000,update_clock)


# Time
# name=Label(root, text="CURRENT WEATHER",font=("arial",15,"bold"))
# name.place(x=340,y=40)
# clock=Label(root,font=("Helvetica",20))
# clock.place(x=340,y=70)


# Enlazar eventos
my_canvas.tag_bind(button, "<Enter>", on_enter)
my_canvas.tag_bind(button, "<Leave>", on_leave)
my_canvas.tag_bind(button, "<ButtonPress-1>", on_click)
my_canvas.tag_bind(button, "<ButtonRelease-1>", on_release)

# myicon=Button(image=search_icon,borderwidth=3,cursor="hand2",bg="#bbbbbb",command=weather_app)
# myicon.place(x=130,y=200)



# # Add labels

# # Time
# name=my_canvas.create_text(400,40, text="CURRENT WEATHER", font=("arial",15,"bold"))
# # name=Label(root, text="CURRENT WEATHER",font=("arial",15,"bold"))
# # name.place(x=340,y=40)
# clock=my_canvas.create_text(340,70, text="00:00", font=("Helvetica",20))
# # clock=Label(root,font=("Helvetica",20))
# # clock.place(x=340,y=70)

# # clock_window=my_canvas.create_window(340,70,window=clock)

# # def update_clock():
# #     current_time=datetime.now().strftime("%I:%M %p")
# #     my_canvas.itemconfig(clock, text=current_time)
# #     root.after(1000,update_clock)


# # Time
# name=Label(root, text="CURRENT WEATHER",font=("arial",15,"bold"))
# name.place(x=340,y=40)
# clock=Label(root,font=("Helvetica",20))
# clock.place(x=340,y=70)


# # Entries
# entry_city=tk.Entry(root,justify="center",width=21,font=("poppins",16,"bold"),bg="#404040",border=0,fg="gray")
# entry_city.insert(0, "City")
# entry_city.place(x=35,y=42)

# entry_city.bind("<FocusIn>", on_focus_in_city)
# entry_city.bind("<FocusOut>", on_focus_out_city)

# entry_country_code=tk.Entry(root,justify="center",width=21,font=("poppins",16,"bold"),bg="#404040",border=0,fg="gray")
# entry_country_code.insert(0, "Country Code (mx,us)")
# entry_country_code.place(x=35,y=102)

# entry_country_code.bind("<FocusIn>", on_focus_in_country)
# entry_country_code.bind("<FocusOut>", on_focus_out_country)

# entry_zip_code=tk.Entry(root,justify="center",width=21,font=("poppins",16,"bold"),bg="#404040",border=0,fg="gray")
# entry_zip_code.insert(0, "ZIP Code")
# entry_zip_code.place(x=35,y=162)

# entry_zip_code.bind("<FocusIn>", on_focus_in_zip)
# entry_zip_code.bind("<FocusOut>", on_focus_out_zip)

# # Focus in/out info
# w_dots=Label(root,text="...",font=("arial",18,"bold"),bg="#1ab5ef")
# w_dots.place(x=411,y=390)
# w_dots.bind("<FocusIn>", on_focus_in_wind)
# w_dots.bind("<FocusOut>", on_focus_out_wind)

# h_dots=Label(root,text="...",font=("arial",18,"bold"),bg="#1ab5ef")
# h_dots.place(x=565,y=390)
# h_dots.bind("<FocusIn>",on_focus_in_humidity)
# h_dots.bind("<FocusOut>",on_focus_out_humidity)

# p_dots=Label(root,text="...",font=("arial",18,"bold"),bg="#1ab5ef")
# p_dots.place(x=742,y=390)
# p_dots.bind("<FocusIn>",on_focus_in_pressure)
# p_dots.bind("<FocusOut>",on_focus_out_pressure)



# # Labels Info
# label1=Label(root,text="WIND",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
# label1.place(x=395,y=350)

# label2=Label(root,text="HUMIDITY",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
# label2.place(x=530,y=350)

# label4=Label(root,text="PRESSURE",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
# label4.place(x=700,y=350)

# t=Label(font=("arial",70,"bold"),fg="#ee666d")
# t.place(x=400,y=140)
# tmin=Label(font=("arial",15,"bold"))
# tmin.place(x=560,y=160)
# tmax=Label(font=("arial",15,"bold"))
# tmax.place(x=560,y=200)
# d=Label(font=("arial",18,"bold"))
# d.place(x=410,y=250)


# w=Label(font=("arial",18,"bold"),bg="#1ab5ef")
# w.place(x=380,y=390)
# h=Label(font=("arial",18,"bold"),bg="#1ab5ef")
# h.place(x=560,y=390)
# p=Label(font=("arial",18,"bold"),bg="#1ab5ef")
# p.place(x=705,y=390)





root.mainloop()