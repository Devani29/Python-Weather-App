from tkinter import Canvas
from PIL import Image, ImageTk


def create_ui_elements(root):
    root.images = {}
    # Background
    weather_bg = Image.open("assets/images/bg_weather.jpg").resize((900, 500))
    root.images["weather_bg_tk"] = ImageTk.PhotoImage(weather_bg)
    
    my_canvas = Canvas(root, width=900, height=500, highlightthickness=0)
    my_canvas.pack(fill="both", expand=True)
    my_canvas.create_image(0,0, image=root.images["weather_bg_tk"], anchor="nw")

    # Search bar
    for i, y in enumerate([20, 80, 140]):
        search_image=Image.open("assets/images/search.png").resize((290,60))
        root.images[f"search_images_{i}"]=ImageTk.PhotoImage(search_image)
        my_canvas.create_image(18, y, image=root.images[f"search_images_{i}"], anchor="nw")


    # Search icon
    search_icon=Image.open("assets/images/search_icon.png").resize((40,40))
    root.images["search_icon_tk"]=ImageTk.PhotoImage(search_icon)

    # my_canvas.create_image(138,200, image=search_icon_tk, anchor="nw")
    button=my_canvas.create_image(138,200, image=root.images["search_icon_tk"], anchor="nw")

    # Box info
    box_info=Image.open("assets/images/box.png").resize((550,180))
    box_info_data=box_info.getdata()
    new_data=[(r,g,b, int(a * 0.25)) for r,g,b, a in box_info_data]
    box_info.putdata(new_data)
    # box_info_tk=ImageTk.PhotoImage(box_info)

    root.images["box_info_tk"] = ImageTk.PhotoImage(box_info)
    my_canvas.create_image(325,280, image=root.images["box_info_tk"], anchor="nw")

    # Logo
    logo=Image.open("assets/images/logo.png")
    root.images["logo_tk"]=ImageTk.PhotoImage(logo)
    my_canvas.create_image(35,250, image=root.images["logo_tk"], anchor="nw")

    return my_canvas, button