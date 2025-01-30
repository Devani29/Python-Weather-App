# Crear el Canvas
my_canvas = Canvas(root, width=900, height=500)
my_canvas.pack(fill="both", expand=True)

# Crear el reloj como texto en el Canvas
clock_text = my_canvas.create_text(340, 70, text="00:00", font=("Helvetica", 20), fill="black")

# Actualizar el texto del reloj
def update_clock():
    current_time = datetime.now().strftime("%I:%M %p")  # Hora actual
    my_canvas.itemconfig(clock_text, text=current_time)  # Actualiza el texto del reloj
    root.after(1000, update_clock)  # Llama a esta función cada 1000 ms (1 segundo)

# Llamar a la función para actualizar el reloj
update_clock()

root.mainloop()