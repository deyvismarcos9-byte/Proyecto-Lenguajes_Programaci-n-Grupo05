# Proyecto Lenguajes de Programación - Grupo 05

Aplicación de escritorio para la gestión de pacientes, citas y consultas del Centro de Salud Ganímedes.

## Descripción

Este proyecto está desarrollado en Python con interfaz gráfica mediante Tkinter y está organizado por capas para separar la lógica de negocio, acceso a datos y presentación.

La aplicación permite gestionar de forma centralizada:

- Registro de pacientes
- Búsqueda de pacientes
- Registro de citas
- Consulta de historial clínico
- Acceso a una interfaz principal desde la cual se seleccionan estas acciones

## Objetivo

Brindar una solución simple y funcional para administrar información médica básica dentro de un centro de salud, utilizando una estructura modular que facilita el mantenimiento y la ampliación del sistema.

## Estructura del proyecto

```text
Proyecto-Lenguajes_Programaci-n-Grupo05/
├── main.py
├── README.md
├── business/
│   └── __init__.py
├── data_access/
│   └── __init__.py
├── database/
├── presentation/
│   ├── __init__.py
│   ├── assets/
│   └── views/
│       ├── index.py
│       ├── registrar_paciente.py
│       ├── buscar_paciente.py
│       ├── registrar_cita.py
│       └── consultar_historial.py
└── .gitignore
```

## Requisitos

- Python 3.8 o superior
- Tkinter (incluido normalmente con Python)
- Sistema operativo compatible con tkinter (Windows, Linux o macOS)

## Instalación

1. Clona este repositorio.
2. Abre una terminal en la carpeta del proyecto.
3. Verifica que Python esté instalado:

```bash
python --version
```

4. Ejecuta la aplicación:

```bash
python main.py
```

## Ejecución

Al iniciar la aplicación se muestra una ventana principal con opciones para:

- Registrar paciente
- Buscar paciente
- Registrar cita
- Consultar historial

La interfaz inicial se encuentra en `presentation/views/index.py` y se lanza desde `main.py`.

## Autoría

Proyecto desarrollado por el Grupo 05 de Lenguajes de Programación.