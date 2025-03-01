import tkinter as tk
import os
import sys
import logging
from tkinter import *
from utils.log import logging_config
from modules.focus_events import (on_focus_in_city, on_focus_out_city,
                          on_focus_in_country, on_focus_out_country,
                          on_focus_in_zip, on_focus_out_zip)
from modules.focus_events import entry_fields
from modules.button_events import on_enter, on_leave, on_click, on_release, create_shadows
from modules.ui_elements import create_ui_elements
from modules.labels_elements import create_labels
from modules.weather_service import fetch_weather, extract_weather_data

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

def run_app():
    root = tk.Tk()
    root.title("Banana's Weather App")
    root.geometry("900x500+300+200")
    root.resizable(False, False)
    root.iconbitmap('src/assets/images/icono.ico')

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)


# Weather App
    def weather_app():
        city = entry_city.get().strip()
        country_code = entry_country_code.get().strip()
        zip_code = entry_zip_code.get().strip()

        data = fetch_weather(city, country_code, zip_code)
        weather_info = extract_weather_data(data)

        if weather_info:
            my_canvas.itemconfig(clock, text=weather_info["local_time"])
            my_canvas.itemconfig(name_city, text=weather_info["city_name"])
            my_canvas.itemconfig(t, text=f"{weather_info['temp']}°")
            my_canvas.itemconfig(tmin, text=f"Minimum temperature {weather_info['temp_min']}°")
            my_canvas.itemconfig(tmax, text=f"Maximum temperature {weather_info['temp_max']}°")
            my_canvas.itemconfig(d, text=f"{weather_info['description']} | Feels like {weather_info['feels_like']}°")
            my_canvas.itemconfig(w, text=f"{weather_info['wind']}km/h")
            my_canvas.itemconfig(h, text=f"{weather_info['humidity']}%")
            my_canvas.itemconfig(p, text=f"{weather_info['pressure']}hPa")


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

    # Button events
    my_canvas.tag_bind(button, "<Enter>", lambda event: on_enter(event, my_canvas, root.shadow_white_tk, button))
    my_canvas.tag_bind(button, "<Leave>", lambda event: on_leave(event, my_canvas))
    my_canvas.tag_bind(button, "<ButtonPress-1>", lambda event: on_click(event, my_canvas, root.shadow_black_tk, button))
    my_canvas.tag_bind(button, "<ButtonRelease-1>", lambda event: on_release(event, my_canvas, weather_app))


    root.mainloop()