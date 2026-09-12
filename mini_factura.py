import tkinter as tk
from tkinter import messagebox, ttk


def calcular_factura(cantidad, precio):
	subtotal = cantidad * precio
	igv = subtotal * 0.18
	total = subtotal + igv
	return subtotal, igv, total


def calcular_y_mostrar():
	try:
		cantidad = float(cantidad_var.get())
		precio = float(precio_var.get())

		if cantidad <= 0 or precio < 0:
			raise ValueError
	except ValueError:
		messagebox.showerror(
			"Datos no válidos",
			"Ingresa una cantidad mayor que 0 y un precio válido.",
		)
		return

	subtotal, igv, total = calcular_factura(cantidad, precio)
	subtotal_var.set(f"S/ {subtotal:.2f}")
	igv_var.set(f"S/ {igv:.2f}")
	total_var.set(f"S/ {total:.2f}")


def limpiar_formulario():
	descripcion_var.set("")
	cantidad_var.set("")
	precio_var.set("")
	subtotal_var.set("S/ 0.00")
	igv_var.set("S/ 0.00")
	total_var.set("S/ 0.00")
	descripcion_entry.focus()


ventana = tk.Tk()
ventana.title("Mini factura")
ventana.geometry("420x390")
ventana.resizable(False, False)

descripcion_var = tk.StringVar()
cantidad_var = tk.StringVar()
precio_var = tk.StringVar()
subtotal_var = tk.StringVar(value="S/ 0.00")
igv_var = tk.StringVar(value="S/ 0.00")
total_var = tk.StringVar(value="S/ 0.00")

contenedor = ttk.Frame(ventana, padding=24)
contenedor.pack(fill="both", expand=True)

ttk.Label(contenedor, text="MINI FACTURA", font=("Segoe UI", 18, "bold")).pack(
	pady=(0, 20)
)

formulario = ttk.Frame(contenedor)
formulario.pack(fill="x")
formulario.columnconfigure(1, weight=1)

ttk.Label(formulario, text="Descripción:").grid(row=0, column=0, sticky="w", pady=6)
descripcion_entry = ttk.Entry(formulario, textvariable=descripcion_var, width=32)
descripcion_entry.grid(row=0, column=1, sticky="ew", pady=6)

ttk.Label(formulario, text="Cantidad:").grid(row=1, column=0, sticky="w", pady=6)
ttk.Entry(formulario, textvariable=cantidad_var, width=32).grid(
	row=1, column=1, sticky="ew", pady=6
)

ttk.Label(formulario, text="Precio (S/):").grid(row=2, column=0, sticky="w", pady=6)
ttk.Entry(formulario, textvariable=precio_var, width=32).grid(
	row=2, column=1, sticky="ew", pady=6
)

ttk.Separator(contenedor).pack(fill="x", pady=18)

resultados = ttk.Frame(contenedor)
resultados.pack(fill="x")
resultados.columnconfigure(1, weight=1)

ttk.Label(resultados, text="Subtotal:").grid(row=0, column=0, sticky="w", pady=5)
ttk.Label(resultados, textvariable=subtotal_var).grid(row=0, column=1, sticky="e", pady=5)
ttk.Label(resultados, text="IGV (18%):").grid(row=1, column=0, sticky="w", pady=5)
ttk.Label(resultados, textvariable=igv_var).grid(row=1, column=1, sticky="e", pady=5)
ttk.Label(resultados, text="Total:", font=("Segoe UI", 11, "bold")).grid(
	row=2, column=0, sticky="w", pady=(10, 5)
)
ttk.Label(resultados, textvariable=total_var, font=("Segoe UI", 11, "bold")).grid(
	row=2, column=1, sticky="e", pady=(10, 5)
)

botones = ttk.Frame(contenedor)
botones.pack(fill="x", pady=(20, 0))
ttk.Button(botones, text="Calcular", command=calcular_y_mostrar).pack(
	side="left", expand=True, fill="x", padx=(0, 6)
)
ttk.Button(botones, text="Limpiar", command=limpiar_formulario).pack(
	side="left", expand=True, fill="x", padx=(6, 0)
)

descripcion_entry.focus()
ventana.bind("<Return>", lambda event: calcular_y_mostrar())
ventana.mainloop()
