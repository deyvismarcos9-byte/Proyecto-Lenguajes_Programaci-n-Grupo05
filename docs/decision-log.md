# Validación técnica de persistencia

## Prueba ejecutada

Se ejecuta:

```text
python -m unittest discover -s tests -v
```

La prueba usa SQLite en memoria y verifica el flujo mínimo que conecta el registro con la búsqueda de pacientes:

1. Crear la tabla mediante `PacienteRepository`.
2. Registrar un paciente.
3. Recuperarlo por DNI.
4. Comprobar que la tupla mantiene las posiciones consumidas por `buscar_paciente.py`.
5. Comprobar que un DNI inexistente devuelve `None`.

## Veredicto

**Viable con alcance acotado.** La persistencia SQLite y el contrato actual del repositorio funcionan de extremo a extremo sin depender de la ventana Tkinter ni de la base de datos local. La evidencia es la ejecución exitosa de las dos pruebas del experimento.

Esta prueba no valida todavía la navegación de la GUI, la validación de datos ingresados ni la integración de citas e historial.

## Decisión y ajuste del plan

- Mantener SQLite y `PacienteRepository` como base de la siguiente iteración.
- No cambiar el contrato posicional mientras las vistas existentes lo consuman.
- Siguiente prioridad: extraer y probar las validaciones de negocio antes de conectarlas a Tkinter.
- Después: repetir una prueba de integración equivalente para citas e historial y realizar una verificación manual de navegación de la GUI.