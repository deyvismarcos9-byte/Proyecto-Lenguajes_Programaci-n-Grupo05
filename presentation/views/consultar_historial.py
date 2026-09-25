import tkinter as tk
from tkinter import messagebox, ttk

import presentation.views.index as index


def show(data_access):
	window = tk.Tk()
	window.title('Consultar historial de citas')
	window.geometry('760x500')
	window.resizable(False, False)
	window.iconbitmap('presentation/assets/icon.ico')

	window.update_idletasks()
	x = (window.winfo_screenwidth() - window.winfo_width()) // 2
	y = (window.winfo_screenheight() - window.winfo_height()) // 2
	window.geometry(f'+{x}+{y}')

	ttk.Label(window, text='Citas del paciente', font=('Arial', 18, 'bold')).pack(pady=(20, 14))

	search_frame = ttk.Frame(window, padding=(28, 8))
	search_frame.pack(fill='x')
	ttk.Label(search_frame, text='DNI del paciente').pack(side='left', padx=(0, 10))
	dni_entry = ttk.Entry(search_frame, width=30)
	dni_entry.pack(side='left', padx=(0, 10))
	ttk.Button(search_frame, text='Buscar', command=lambda: buscar_citas()).pack(side='left')

	patient_label = ttk.Label(window, text='')
	patient_label.pack(anchor='w', padx=30, pady=(10, 8))

	columns = ('fecha', 'hora', 'motivo')
	appointments = ttk.Treeview(window, columns=columns, show='headings', height=14)
	appointments.heading('fecha', text='Fecha')
	appointments.heading('hora', text='Hora')
	appointments.heading('motivo', text='Motivo')
	appointments.column('fecha', width=130, anchor='center')
	appointments.column('hora', width=100, anchor='center')
	appointments.column('motivo', width=450, anchor='w')
	appointments.pack(fill='both', expand=True, padx=30, pady=(0, 8))

	footer = ttk.Frame(window, padding=(30, 0, 30, 14))
	footer.pack(side='bottom', fill='x')
	status_label = ttk.Label(footer, text='Ingrese el DNI para consultar las citas.')
	status_label.pack(side='left', anchor='w')

	def buscar_citas():
		dni = dni_entry.get().strip()
		if not dni:
			messagebox.showwarning('Dato requerido', 'Ingrese el DNI del paciente.', parent=window)
			return

		paciente = data_access.paciente_repository.get_paciente_by_dni(dni)
		for row in appointments.get_children():
			appointments.delete(row)

		if paciente is None:
			patient_label.config(text='')
			status_label.config(text='No se encontró un paciente con ese DNI.')
			return

		patient_label.config(text=f'Paciente: {paciente[2]} {paciente[3]}  |  ID: {paciente[0]}')
		citas = data_access.cita_repository.get_citas_by_paciente_id(paciente[0])
		for cita in citas:
			appointments.insert('', tk.END, values=(cita[1], cita[2], cita[3]))
		status_label.config(
			text=f'{len(citas)} cita(s) encontrada(s).' if citas else 'Este paciente no tiene citas registradas.'
		)

	def volver():
		window.destroy()
		index.show(data_access)

	ttk.Button(footer, text='Volver', command=volver).pack(side='right')
	window.bind('<Return>', lambda event: buscar_citas())
	dni_entry.focus_set()
	window.mainloop()