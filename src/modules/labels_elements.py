from tkinter import Canvas

def create_labels(my_canvas):
    # Time
    clock = my_canvas.create_text(390,70, text="00:00", font=("Helvetica",20))
    name = my_canvas.create_text(430,40, text="CURRENT WEATHER", font=("arial",15,"bold"))
    name_city = my_canvas.create_text(600, 100, text="", font=("arial", 18, "bold"))

    t = my_canvas.create_text(470, 170, text="", font=("arial",70,"bold"), fill="#ec3d46")
    tmin = my_canvas.create_text(680, 154, text="", font=("arial",15,"bold"))
    tmax = my_canvas.create_text(682, 186, text="", font=("arial",15,"bold"))
    d = my_canvas.create_text(600, 250, text="", font=("arial",18,"bold"))

    label_wind = my_canvas.create_text(420, 345, text="WIND", font=("Helvetica",15,'bold'), fill="white")
    label_hum = my_canvas.create_text(580, 345, text="HUMIDITY", font=("Helvetica",15,'bold'), fill="white")
    label_pre = my_canvas.create_text(760, 345, text="PRESSURE", font=("Helvetica",15,'bold'), fill="white")

    w = my_canvas.create_text(418, 395, text="---", font=("arial",18,"bold"))
    h = my_canvas.create_text(580, 395, text="---", font=("arial",18,"bold"))
    p = my_canvas.create_text(760, 395, text="---", font=("arial",18,"bold"))


    return clock, name, name_city, t, tmin, tmax, d, label_wind, label_hum, label_pre, w, h, p