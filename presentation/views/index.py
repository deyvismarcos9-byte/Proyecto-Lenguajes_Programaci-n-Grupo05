import tkinter as tk
from tkinter import ttk

def show():
    window = tk.Tk()
    window.title('Programa de Gestión del Centro de Salud Ganímedes')
    window.geometry('640x480')
    window.resizable(False, False)

    window.iconbitmap('presentation/assets/icon.ico')

    # Centrando la ventana en la pantalla
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    title_label = ttk.Label(window, text='Escoja que desea hacer', font=('Arial', 16))
    title_label.pack(pady=20)

    button_1 = ttk.Button(window, text='Registrar paciente', command=lambda: print('Registrar paciente'))
    button_1.pack(pady=10, fill='x', padx=40, ipady=20)

    button_2 = ttk.Button(window, text='Buscar paciente', command=lambda: print('Buscar paciente'))
    button_2.pack(pady=10, fill='x', padx=40, ipady=20)

    button_3 = ttk.Button(window, text='Registrar cita', command=lambda: print('Registrar cita'))
    button_3.pack(pady=10, fill='x', padx=40, ipady=20)

    button_4 = ttk.Button(window, text='Consultar historial', command=lambda: print('Consultar historial'))
    button_4.pack(pady=10, fill='x', padx=40, ipady=20)

    window.mainloop()