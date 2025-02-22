import tkinter as tk
from PIL import Image, ImageDraw, ImageTk

shadow_white = None
shadow_black = None

# Show shadow
def on_enter(event, my_canvas, shadow_white_tk, button, *args):
    global shadow_white
    if shadow_white is None:
        shadow_white = my_canvas.create_image(133,196, image=shadow_white_tk, anchor="nw")
        my_canvas.tag_lower(shadow_white, button)  

# Hide shadow
def on_leave(event, my_canvas, *args):
    global shadow_white
    if shadow_white:
        my_canvas.delete(shadow_white)
        shadow_white = None

def on_click(event, my_canvas, shadow_black_tk, button, *args):
    global shadow_black
    if shadow_black is None:
        shadow_black = my_canvas.create_image(133,196, image=shadow_black_tk, anchor="nw")
        my_canvas.tag_lower(shadow_black, button)
    print("click")

def on_release(event, my_canvas, weather_app, *args):
    global shadow_black
    if shadow_black:
        my_canvas.delete(shadow_black)
        shadow_black = None
    print("release")
    weather_app()


def create_shadows(root):
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


    root.shadow_refs = {
        "shadow_white_tk": shadow_white_tk,
        "shadow_black_tk": shadow_black_tk
    }

    return root.shadow_refs
        