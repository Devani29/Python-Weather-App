from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
from PIL import Image, ImageTk 
from ctypes import windll

root=tk.Tk()
root.title("Banana's Weather App")
root.geometry("900x500+300+200")
root.resizable(False,False)
root.iconbitmap('icono.ico')

# Root rounded border 
GWL_STYLE = -16               # Modify window style -16 it's the value for the windows style in the Windows API
WS_CAPTION = 0x00C00000       # Enables window title bar 
WS_THICKFRAME = 0x00040000    # Enables window border, it can be use to make rounded borders

hwnd = windll.user32.GetParent(root.winfo_id())            # Gets ID of the app main window, root is the window creared by tkinter
style = windll.user32.GetWindowLongW(hwnd, GWL_STYLE)      # Use the hwnd window handle to get the current windoe style
style |= WS_CAPTION | WS_THICKFRAME                        # The operator |= is used to add the WS_CAPTION(title bar) and WS_THICKFRAME(rounded border) styles
windll.user32.SetWindowLongW(hwnd, GWL_STYLE, style)       # The window style is uptaded with the new values


# Define background
weather_bg = Image.open("bg_weather.jpg").resize((900, 500))
weather_bg_tk = ImageTk.PhotoImage(weather_bg)

# Create a canvas
my_canvas = tk.Canvas(root, width=900, height=500, highlightthickness=0)
my_canvas.pack(fill="both", expand=True)

# Set image in canvas
my_canvas.create_image(0,0, anchor="nw", image=weather_bg_tk)

# Crear un Label con la imagen de fondo
label_fondo = tk.Label(root, image=weather_bg_tk)
label_fondo.place(x=0, y=0, relwidth=1, relheight=1)



root.mainloop()