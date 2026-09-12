import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from data_access import DataAccess

import presentation.views.index as index

def show():
    window = tk.Tk()
    window.title('Buscar paciente')
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

    title_label = ttk.Label(window, text='Buscar paciente', font=('Arial', 18, 'bold'))
    title_label.pack(pady=(20, 15))

    form_frame = ttk.Frame(window, padding=20)
    form_frame.pack(fill='both', expand=True, padx=30)

    fields = [
        ('DNI', 'normal'),
        ('ID', 'readonly'),
        ('Nombre', 'readonly'),
        ('Apellido', 'readonly'),
        ('Fecha de nacimiento', 'readonly'),
        ('Dirección', 'readonly'),
        ('Teléfono', 'readonly'),
    ]

    entries = {}

    for label_text, state in fields:
        row = ttk.Frame(form_frame)
        row.pack(fill='x', pady=6)

        label = ttk.Label(row, text=label_text, width=25, anchor='w')
        label.pack(side='left')

        var = tk.StringVar()
        entry = ttk.Entry(row, width=50, state=state, textvariable=var)
        entry.pack(side='left', fill='x', expand=True)
        entries[label_text] = (var, entry)

    buttons_frame = ttk.Frame(window)
    buttons_frame.pack(pady=(10, 25))

    def buscar_paciente():
        dni = entries['DNI'][0].get().strip()
        if not dni:
            messagebox.showwarning('Datos incompletos', 'Debe ingresar un DNI para buscar al paciente.')
            return

        try:
            data_access = DataAccess()
            paciente = data_access.paciente_repository.get_paciente_by_dni(dni)

            if paciente:
                entries['ID'][0].set(paciente[0])
                entries['Nombre'][0].set(paciente[2])
                entries['Apellido'][0].set(paciente[3])
                entries['Fecha de nacimiento'][0].set(paciente[4])
                entries['Dirección'][0].set(paciente[5])
                entries['Teléfono'][0].set(paciente[6])
            else:
                messagebox.showinfo("Paciente no encontrado", f"No se encontró un paciente con DNI: {dni}")
                entries['ID'][0].set('')
                entries['Nombre'][0].set('')
                entries['Apellido'][0].set('')
                entries['Fecha de nacimiento'][0].set('')
                entries['Dirección'][0].set('')
                entries['Teléfono'][0].set('')
        except Exception as exc:
            messagebox.showerror('Error al buscar paciente', f'Ocurrió un error al consultar los datos: {exc}')

    def goto_index():
        window.destroy()
        index.show()

    ttk.Button(buttons_frame, text='Actualizar', command=buscar_paciente).pack(side='left', padx=10)
    ttk.Button(buttons_frame, text='Volver', command=goto_index).pack(side='left', padx=10)

    window.mainloop()