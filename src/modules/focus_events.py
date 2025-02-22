import tkinter as tk

def on_focus_in_city(event):
    if event.widget.get() == "City":
        event.widget.delete(0, tk.END)
        event.widget.config(fg="white")

def on_focus_out_city(event):
    if event.widget.get() == "":
        event.widget.insert(0, "City")
        event.widget.config(fg="gray")

def on_focus_in_country(event):
    if event.widget.get() == "Country Code (mx,us)":
        event.widget.delete(0, tk.END)
        event.widget.config(fg="white")

def on_focus_out_country(event):
    if event.widget.get() == "":
        event.widget.insert(0, "Country Code (mx,us)")
        event.widget.config(fg="gray")

def on_focus_in_zip(event):
    if event.widget.get() == "ZIP Code":
        event.widget.delete(0, tk.END)
        event.widget.config(fg="white")

def on_focus_out_zip(event):
    if event.widget.get() == "":
        event.widget.insert(0, "ZIP Code")
        event.widget.config(fg="gray")


def entry_fields(root, my_canvas):
    entry_city=tk.Entry(root, justify="center", width=21, font=("poppins",16,"bold"), 
                        bg="#23333d", border=0, fg="gray", highlightthickness=0, insertbackground="black")
    entry_city.insert(0, "City")
    entry_window=my_canvas.create_window(35,38, window=entry_city, anchor="nw")

    entry_city.bind("<FocusIn>", on_focus_in_city)
    entry_city.bind("<FocusOut>", on_focus_out_city)

    entry_country_code=tk.Entry(root, justify="center", width=21, font=("poppins",16,"bold"), 
                                bg="#202e3b", border=0, fg="gray", highlightthickness=0, insertbackground="black")
    entry_country_code.insert(0, "Country Code (mx,us)")
    entry_window2=my_canvas.create_window(35,98, window=entry_country_code, anchor="nw")

    entry_country_code.bind("<FocusIn>", on_focus_in_country)
    entry_country_code.bind("<FocusOut>", on_focus_out_country)

    entry_zip_code=tk.Entry(root, justify="center", width=21, font=("poppins",16,"bold"), 
                            bg="#1d2b37", border=0, fg="gray", highlightthickness=0, insertbackground="black")
    entry_zip_code.insert(0, "ZIP Code")
    entry_window3=my_canvas.create_window(35,158, window=entry_zip_code, anchor="nw")

    entry_zip_code.bind("<FocusIn>", on_focus_in_zip)
    entry_zip_code.bind("<FocusOut>", on_focus_out_zip)

    return entry_city, entry_country_code, entry_zip_code
