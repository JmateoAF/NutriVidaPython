# NutriVidaPython

**Sistema de Gestión y Seguimiento Nutricional**  
*Proyecto Integrador — Lenguajes de Programación (Python & Scala)*  
**Universidad de Cuenca — Facultad de Ingeniería**  
**Proyecto realizado por:** *Jostin Aucancela y José Tenesaca*

---

## Descripción del Proyecto

NutriVida es un sistema informático desarrollado bajo la arquitectura **Modelo-Vista-Controlador (MVC)** enfocado en la gestión de información alimentaria y el seguimiento nutricional personalizado. El sistema permite registrar el consumo diario de alimentos, calcular valores nutricionales automáticos, evaluar el cumplimiento de objetivos y generar reportes detallados utilizando enfoques de Programación Orientada a Objetos (POO) y Programación Funcional.

---

## Requisitos Previos

* **Python 3.10+** instalado en el sistema.
* **Git** configurado.
* *(Solo en Linux)* Paquetes de dependencias del sistema para PyQt6:
  ```
  sudo apt update
  sudo apt install libxcb-cursor0
  ```

---

## Guía de Instalación y Configuración Paso a Paso

Para evitar problemas de compatibilidad en **Linux** o **Windows**, y garantizar que funcione en cualquier IDE (**IntelliJ IDEA**, **PyCharm** o **Visual Studio Code**), sigue las instrucciones según tu entorno.

### 1. Clonar el Repositorio

```
git clone https://github.com/JmateoAF/NutriVidaPython.git
cd NutriVidaPython
```

---

### 2. Configuración del Entorno Virtual (VENV)

El entorno virtual es un aislamiento donde se instalan las librerías del proyecto sin afectar el sistema global.

#### Opción A: Desde IntelliJ IDEA
1. Abre la carpeta del proyecto en IntelliJ.
2. Si detecta un proyecto de Python, el IDE te sugerirá crear un **Virtualenv** automáticamente.

#### Opción B: Desde VS Code / Terminal (Linux & Windows)
Si clonas el proyecto desde Visual Studio Code o la terminal, debes crear el entorno virtual manualmente:

* **Crear el entorno virtual:**
    ```
    python3 -m venv .venv
    ```

* **En Linux / macOS:**
  ```
  source .venv/bin/activate
  ```

* **En Windows:**
  ```
  .\.venv\Scripts\Activate.ps1
  ```
  
Con esto activaras los entornos virtuales dependiendo en que sistema operativo estés
 
**Nota sobre VS Code:** Una vez activado/creado el `.venv`, presiona `Ctrl + Shift + P` (o `Cmd + Shift + P` en Mac), busca **Python: Select Interpreter** y elige el intérprete dentro de `.venv`.

---

### 3. Instalación de Dependencias

Con el entorno virtual **activado**, ejecuta el siguiente comando para instalar todas las librerías requeridas (incluyendo PyQt6):

```
pip install -r requirements.txt
```

---

## Estructura del Proyecto (Patrón MVC)

```text
NutriVidaPython/
│
├── data/                  # Almacenamiento persistente (archivos binarios/JSON)
├── modelo/                # Clases de dominio, entidades y lógica de datos
├── vista/                 # Interfaces gráficas con PyQt6 (ej. VistaPersona.py)
├── controlador/           # Lógica de negocio y mediación entre Vista y Modelo
│
├── .gitignore             # Ignora .venv, __pycache__ y datos temporales
├── main.py                # Punto de entrada de la aplicación
├── README.md              # Documentación del proyecto
└── requirements.txt       # Lista de dependencias de Python
```

---

## Especificaciones Técnicas del Proyecto

1. **Arquitectura:** Modelo-Vista-Controlador (MVC).
2. **Interfaz Gráfica:** PyQt6.
3. **Programación Funcional:** Uso de funciones de orden superior (`map`, `filter`, `reduce`).
4. **Persistencia:** Guardado binario permanente en la carpeta `data/`.
5. **Reportes Integrados:**
   * 2 Reportes con filtrado de datos (`filter`).
   * 1 Reporte con agrupaciones/clasificaciones.
   * 1 Reporte de valores calculados/acumulados (`reduce`).
   * 1 Reporte combinado relacional.