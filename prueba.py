# Crear la ventana principal
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

# Set image
weather_bg = Image.open("bg_weather.jpg")
weather_bg = weather_bg.resize((900, 500))
weather_bg_tk = ImageTk.PhotoImage(weather_bg)

# Create a canvas
my_canvas = Canvas(root, width=900, height=500, highlightthickness=0)
my_canvas.pack(fill="both", expand=True)

# # Set image in canvas
my_canvas.create_image(0,0, image=weather_bg_tk, anchor="nw")

root.mainloop()