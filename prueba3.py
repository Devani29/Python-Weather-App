# background= Background color
# foreground= Text color
# width= 
# height=
# higlightthickness= Thickness of the focus border
# hichlightbackground= Color of the border when is not focused
# highlitchcolor= Color of the focus border when focused
# activebackground= Background color when the widget is active
# activeforeground= Color of the text when the widget is active
# cursor= Type of cursor when the mouse hovers over the widget
# border= 

from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
from PIL import Image, ImageTk, ImageDraw
from ctypes import windll

root=tk.Tk()
root.title("Banana's Weather App")
root.geometry("900x500+300+200")
root.resizable(False,False)
root.iconbitmap('icono.ico')

my_canvas = Canvas(root, width=900, height=500, highlightthickness=0)
my_canvas.pack(fill="both", expand=True)

# Define background
weather_bg = Image.open("bg_weather.jpg").resize((900, 500))
weather_bg_tk = ImageTk.PhotoImage(weather_bg)

# Set image in canvas
my_canvas.create_image(0,0, image=weather_bg_tk, anchor="nw")

# Search icon
search_icon=Image.open("search_icon.png").resize((40,40))
search_icon_tk=ImageTk.PhotoImage(search_icon)
button=my_canvas.create_image(130,200, image=search_icon_tk, anchor="nw")

# Black shadows
shadow_black_img = Image.new("RGBA", (50, 50), (0, 0, 0, 100))  # Color negro con 100 de opacidad
draw_black = ImageDraw.Draw(shadow_black_img)
draw_black.rectangle([0, 0, 49, 49], outline=(0, 0, 0, 180), width=2)
shadow_black_tk = ImageTk.PhotoImage(shadow_black_img)

# White shadow
shadow_white_img = Image.new("RGBA", (50,50),(255,255,255,100))
draw_white = ImageDraw.Draw(shadow_white_img)
draw_white.rectangle([0,0,49,49], outline=(255,255,255,100), width=2)
shadow_white_tk = ImageTk.PhotoImage(shadow_white_img)

# Save references 
root.shadow_black_tk = shadow_black_tk
root.shadow_white_tk = shadow_white_tk

# Variable para la sombra
shadow_black = None
shadow_white = None  

# Función para mostrar sombra (con imagen)
def on_enter(event):
    global shadow_black
    if shadow_black is None:
        shadow_black = my_canvas.create_image(125, 196, image=shadow_black_tk, anchor="nw")
        my_canvas.tag_lower(shadow_black, button)  # Mueve la sombra debajo del botón

# Función para ocultar sombra
def on_leave(event):
    global shadow_black
    if shadow_black:
        my_canvas.delete(shadow_black)
        shadow_black = None

def on_click(event):
    global shadow_white
    if shadow_white is None:
        shadow_white = my_canvas.create_image(125,196,image=shadow_white_tk, anchor="nw")
        my_canvas.tag_lower(shadow_white, button)

def on_release(event):
    global shadow_white
    if shadow_white:
        my_canvas.delete(shadow_white)
        shadow_white = None


# Enlazar eventos
my_canvas.tag_bind(button, "<Enter>", on_enter)
my_canvas.tag_bind(button, "<Leave>", on_leave)
my_canvas.tag_bind(button, "<ButtonPress-1>", on_click)
my_canvas.tag_bind(button, "<ButtonRelease-1>", on_release)

# # Shadows
# shadow_black_img = Image.new("RGBA",(50,50),(0,0,0,80))
# draw_black=ImageDraw.Draw(shadow_black_img)
# draw_black.rectangle([0,0,49,49], fill=(0,0,0,100), outline=(0,0,0,100), width=2)
# shadow_black_tk = ImageTk.PhotoImage(shadow_black_img)

# shadow_white_img = Image.new("RGBA",(50,50),(255,255,255,0))
# draw_white=ImageDraw.Draw(shadow_white_img)
# draw_white.rectangle([0,0,49,49], fill=(255, 255, 255, 100), outline=(255,255,255,100), width=2)
# shadow_white_tk = ImageTk.PhotoImage(shadow_white_img)

# root.shadow_black_tk = shadow_black_tk
# root.shadow_white_tk = shadow_white_tk

# shadow_black=my_canvas.create_image(129,199, image=shadow_black_tk, anchor="nw", state="hidden")
# shadow_white=my_canvas.create_image(129,199, image=shadow_white_tk, anchor="nw", state="hidden")


# def on_hover(event):
#     my_canvas.itemconfig(shadow_black, state="normal")

# def on_leave(event):
#     my_canvas.itemconfig(shadow_black, state="hidden")

# def on_click(event):
#     my_canvas.itemconfig(shadow_white, state="normal")

# def on_release(event):
#     my_canvas.itemconfig(shadow_white, state="hidden")


# my_canvas.tag_bind(button, "<Enter>", on_hover)
# my_canvas.tag_bind(button, "<Leave>", on_leave)
# my_canvas.tag_bind(button, "<ButtonPress-1>", on_click)
# my_canvas.tag_bind(button, "<ButtonRelease-1>", on_release)



root.mainloop()