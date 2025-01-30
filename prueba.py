# Crear el Canvas
my_canvas = Canvas(root, width=900, height=500)
my_canvas.pack(fill="both", expand=True)

# Crear un Label para el reloj
clock = Label(root, font=("Helvetica", 20))
clock.place(x=340, y=70)

# Agregar el Label al Canvas usando create_window
clock_window = my_canvas.create_window(340, 70, window=clock)

# Actualizar el texto del reloj
def update_clock():
    current_time = datetime.now().strftime("%I:%M %p")  # Hora actual
    clock.config(text=current_time)  # Actualiza el texto del reloj
    root.after(1000, update_clock)  # Llama a esta función cada 1000 ms (1 segundo)

# Llamar a la función para actualizar el reloj
update_clock()
