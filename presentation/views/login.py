import tkinter as tk
from tkinter import messagebox, ttk

import presentation.views.index as index


def show(data_access):
    window = tk.Tk()
    window.title('Inicio de sesión | Centro de Salud Ganímedes')
    window.geometry('420x370')
    window.resizable(False, False)

    window.update_idletasks()
    x = (window.winfo_screenwidth() - window.winfo_width()) // 2
    y = (window.winfo_screenheight() - window.winfo_height()) // 2
    window.geometry(f'+{x}+{y}')

    repository = data_access.usuario_repository
    first_user = not repository.has_users()

    content = ttk.Frame(window, padding=32)
    content.pack(fill='both', expand=True)
    ttk.Label(content, text='Centro de Salud Ganímedes', font=('Arial', 16, 'bold')).pack(pady=(12, 8))
    heading = ttk.Label(content, font=('Arial', 11))
    heading.pack(pady=(0, 18))

    ttk.Label(content, text='Usuario').pack(anchor='w')
    username_entry = ttk.Entry(content)
    username_entry.pack(fill='x', pady=(4, 12))

    ttk.Label(content, text='Contraseña').pack(anchor='w')
    password_entry = ttk.Entry(content, show='*')
    password_entry.pack(fill='x', pady=(4, 12))

    confirm_entry = None
    if first_user:
        heading.config(text='Crear la primera cuenta')
        ttk.Label(content, text='Confirmar contraseña').pack(anchor='w')
        confirm_entry = ttk.Entry(content, show='*')
        confirm_entry.pack(fill='x', pady=(4, 12))
        button_text = 'Crear cuenta e iniciar sesión'
    else:
        heading.config(text='Inicie sesión para continuar')
        button_text = 'Iniciar sesión'

    def submit(event=None):
        username = username_entry.get()
        password = password_entry.get()
        if first_user:
            assert confirm_entry != None, "FATAL ERROR"
            if password != confirm_entry.get():
                messagebox.showerror('Contraseña', 'Las contraseñas no coinciden.', parent=window)
                return
            try:
                repository.add_usuario(username, password)
            except ValueError as error:
                messagebox.showerror('No se pudo crear la cuenta', str(error), parent=window)
                return
        elif repository.authenticate(username, password) is None:
            messagebox.showerror('Acceso denegado', 'Usuario o contraseña incorrectos.', parent=window)
            password_entry.delete(0, tk.END)
            password_entry.focus_set()
            return

        window.destroy()
        index.show(data_access)

    ttk.Button(content, text=button_text, command=submit).pack(fill='x', pady=(8, 0), ipady=5)
    window.bind('<Return>', submit)
    username_entry.focus_set()
    window.mainloop()