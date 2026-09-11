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

## Arquitectura del sistema

El sistema utiliza una arquitectura organizada por capas, con el propósito de separar las responsabilidades de cada componente y facilitar el mantenimiento y evolución de la aplicación.

### Presentación (`presentation/`)

Contiene la interfaz gráfica desarrollada con Tkinter. Esta capa permite la interacción del usuario con el sistema mediante las diferentes vistas disponibles, como el registro y búsqueda de pacientes, registro de citas y consulta del historial clínico.

### Lógica de negocio (`business/`)

Esta capa concentra las reglas y validaciones relacionadas con los procesos del sistema. Su separación permite mantener la lógica de negocio independiente de la interfaz gráfica.

### Acceso a datos (`data_access/`)

Se encarga de gestionar la comunicación entre la lógica de negocio y la información almacenada. Esta separación permite organizar las operaciones de consulta, registro y actualización de datos.

### Persistencia (`database/`)

Contiene los recursos relacionados con el almacenamiento de la información del sistema, permitiendo centralizar los datos necesarios para la gestión de pacientes, citas y consultas.

Esta organización permite reducir el acoplamiento entre componentes y facilita futuras modificaciones o ampliaciones del sistema.

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
