import tkinter as tk
from tkinter import ttk
import serial
import time

# Establece la conexión con Arduino
try:
    ser = serial.Serial('COM3', 9600)  # Asegúrate de usar el puerto correcto
except:
    print("Error al conectar con Arduino. Verifica el puerto.")

def toggle_relay(command):
    """Envía un comando al Arduino para controlar el relé."""
    ser.write(command.encode())

def activate():
    """Función para activar el relé y el LED."""
    print("Activando relé y LED")
    toggle_relay('1')

def deactivate():
    """Función para desactivar el relé y el LED."""
    print("Desactivando relé y LED")
    toggle_relay('0')

# Crea la ventana principal
root = tk.Tk()
root.title("Control de Relé")

# Agrega un estilo para los botones
style = ttk.Style()
style.configure('my.TButton', font=('Helvetica', 12))

# Botón para activar el relé y el LED
activate_button = ttk.Button(root, text="Activar", command=activate, style='my.TButton')
activate_button.pack(pady=20, padx=20, ipadx=10, ipady=10)

# Botón para desactivar el relé y el LED
deactivate_button = ttk.Button(root, text="Desactivar", command=deactivate, style='my.TButton')
deactivate_button.pack(pady=20, padx=20, ipadx=10, ipady=10)

# Inicia el bucle de eventos
root.mainloop()

# Asegúrate de cerrar la conexión serial al cerrar la ventana
ser.close()
