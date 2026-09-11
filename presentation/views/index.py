import tkinter as tk
from tkinter import ttk
import presentation.views.registrar_paciente as registrar_paciente
import presentation.views.buscar_paciente as buscar_paciente
import presentation.views.registrar_cita as registrar_cita
import presentation.views.consultar_historial as consultar_historial

from presentation.views.not_implemented import show_error

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

    def goto_register_patient():
        window.destroy()
        registrar_paciente.show()

    def goto_search_patient():
        window.destroy()
        buscar_paciente.show()

    def goto_register_appointment():
        window.destroy()
        registrar_cita.show()

    title_label = ttk.Label(window, text='Escoja que desea hacer', font=('Arial', 16))
    title_label.pack(pady=20)

    button_1 = ttk.Button(window, text='Registrar paciente', command=goto_register_patient)
    button_1.pack(pady=10, fill='x', padx=40, ipady=20)

    button_2 = ttk.Button(window, text='Buscar paciente', command=goto_search_patient)
    button_2.pack(pady=10, fill='x', padx=40, ipady=20)

    button_3 = ttk.Button(window, text='Registrar cita', command=goto_register_appointment)
    button_3.pack(pady=10, fill='x', padx=40, ipady=20)

    button_4 = ttk.Button(window, text='Consultar historial', command=show_error)
    button_4.pack(pady=10, fill='x', padx=40, ipady=20)

    window.mainloop()