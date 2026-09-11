import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import presentation.views.index as index

from data_access import DataAccess

def show():
    window = tk.Tk()
    window.title('Registrar cita')
    window.geometry('700x520')
    window.resizable(False, False)

    window.iconbitmap('presentation/assets/icon.ico')

    # Centrando la ventana en la pantalla
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    title_label = ttk.Label(window, text='Registrar cita', font=('Arial', 18, 'bold'))
    title_label.pack(pady=(20, 15))

    form_frame = ttk.Frame(window, padding=20)
    form_frame.pack(fill='both', expand=True, padx=30)

    fields = [
        ('ID Paciente', 'id_paciente'),
        ('Fecha de cita', 'fecha_cita'),
        ('Hora de cita', 'hora_cita'),
        ('Motivo de la cita', 'motivo_cita'),
    ]

    entries = {}

    for label_text, key in fields:
        row = ttk.Frame(form_frame)
        row.pack(fill='x', pady=6)

        label = ttk.Label(row, text=label_text, width=25, anchor='w')
        label.pack(side='left')

        var = tk.StringVar()
        entry = ttk.Entry(row, textvariable=var, width=50)
        entry.pack(side='left', fill='x', expand=True)
        entries[key] = var

    def guardar_paciente():
        datos = {key: value.get().strip() for key, value in entries.items()}

        if any(not valor for valor in datos.values()):
            messagebox.showwarning('Datos incompletos', 'Debe completar todos los campos.')
            return

        data_access = DataAccess()
        data_access.cita_repository.add_cita(
            datos['id_paciente'],
            datos['fecha_cita'],
            datos['hora_cita'],
            datos['motivo_cita']
        )

        messagebox.showinfo('Registro', 'Cita registrada correctamente.')

        for value in entries.values():
            value.set('')

    def goto_index():
        window.destroy()
        index.show()

    buttons_frame = ttk.Frame(window)
    buttons_frame.pack(pady=(10, 25))

    ttk.Button(buttons_frame, text='Guardar', command=guardar_paciente).pack(side='left', padx=10)
    ttk.Button(buttons_frame, text='Volver', command=goto_index).pack(side='left', padx=10)

    window.mainloop()