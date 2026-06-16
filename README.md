<div align="center">
    <h1>Proyecto de Análisis de Datos Modular <br/>+ Regresión Lineal Simple</h1>
    <h3>Dataset: Salary Dataset — Predicción de Salario por Años de Experiencia</h3>
</div>

[DATASET URL: Salary_dataset.csv](https://docs.google.com/spreadsheets/d/e/2PACX-1vQU0SIALScXx8VXDX7yKNKWWPKE1YjFlWc6VTEVSN45CklWWf-uWmprQIyLtoPDA18tX9cFDr-aQ9S6/pubhtml)

## 📊 Descripción del Proyecto

Este proyecto implementa una estructura modular y moderna para el análisis estadístico y modelado de datos (EDA). El objetivo principal es estructurar un flujo de trabajo reproducible que incluye la limpieza de datos, análisis exploratorio e implementación de una **regresión lineal simple** para análisis predictivo.

Todo el ecosistema se administra mediante **uv** como gestor de paquetes de alto rendimiento, **Jupyter Notebooks** embebidos en **VS Code**, y un sistema de auditoría mediante logs automatizados y aislados.

---

## 🛠️ Tecnologías Utilizadas

| Tecnología                                                                                      | Propósito                                              |
| :---------------------------------------------------------------------------------------------- | :----------------------------------------------------- |
| <img src="https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white">         | Lenguaje de programación principal                     |
| <img src="https://img.shields.io/badge/UV-Package%20Manager-E95F9B">                                                                  | Gestor de paquetes y entornos de ultra-alta velocidad  |
| <img src="https://img.shields.io/badge/Pandas-2.0-150458?logo=pandas&logoColor=white">          | Manipulación y análisis estructurado de datos          |
| <img src="https://img.shields.io/badge/NumPy-1.24-013243?logo=numpy&logoColor=white">           | Operaciones numéricas y álgebra lineal matricial       |
| <img src="https://img.shields.io/badge/Matplotlib-3.7-11557C?logo=matplotlib&logoColor=white">  | Creación de gráficos y visualizaciones estáticas       |
| <img src="https://img.shields.io/badge/Seaborn-0.12-388E8E?logo=seaborn&logoColor=white">       | Gráficos estadísticos y de distribución avanzados      |
| <img src="https://img.shields.io/badge/SciPy-1.10-8CAAE6?logo=scipy&logoColor=white">           | Computación científica y pruebas estadísticas (t-test) |
| <img src="https://img.shields.io/badge/Jupyter-F37626?logo=jupyter&logoColor=white">            | Cuadernos interactivos para experimentación            |
| <img src="https://img.shields.io/badge/VS_Code-007ACC?logo=visual-studio-code&logoColor=white"> | Editor de código e interfaz nativa de Notebooks        |
| <img src="https://img.shields.io/badge/Git-F05032?logo=git&logoColor=white">                    | Control de versiones local del repositorio             |
| <img src="https://img.shields.io/badge/GitHub-181717?logo=github&logoColor=white">              | Alojamiento de código y colaboración remota            |

---

## 📂 Estructura del File System

El diseño del proyecto aísla los datos, el código de producción y las bitácoras de ejecución:

```text
nombre_proyecto/
├── .venv/                   # Entorno virtual optimizado administrado por uv
├── .vscode/                 # Configuraciones automatizadas del espacio de trabajo
│   └── settings.json        # Configuración de Kernel, Autoreload dinámico y rutas
├── data/                    # Repositorio local de almacenamiento de datos
│   ├── raw/                 # Datos originales sin procesar (inmutables)
│   └── processed/           # Conjuntos de datos limpios listos para modelado
├── logs/                    # Bitácoras de auditoría de procesos en segundo plano
│   └── proyecto.log         # Archivo persistente con el historial de eventos
├── notebooks/               # Cuadernos de experimentación y visualización
│   └── analisis.ipynb       # Notebook principal de trabajo
├── src/                     # Código fuente empaquetado del proyecto
│   ├── __init__.py          # Expone las funciones modulares
│   └── procesar.py          # Scripts dedicados a la extracción y limpieza
├── pyproject.toml           # Declaración moderna de dependencias (PEP 621)
└── uv.lock                  # Registro estricto y reproducible de dependencias
```

---

## ⚙️ Características Clave Implementadas

- **Instalación Editable Moderna:** Gracias a las configuraciones en `pyproject.toml` (`[dependency-groups]`), la carpeta `src/` se comporta como una librería propia instalada en el entorno virtual. Puedes hacer `from src.procesar import ...` desde cualquier notebook sin alterar `sys.path`.
- **Cero Configuración Manual de Kernels:** VS Code localiza e inicializa de forma automática el intérprete almacenado en `.venv/` al ejecutar una celda.
- **Autoreload Silencioso:** Modifica cualquier archivo `.py` en `src/` y los cambios se reflejarán instantáneamente en tu Jupyter Notebook al volver a correr la celda, configurado de manera nativa mediante el motor subyacente.
- **Logs Aislados de Auditoría:** Las operaciones de lectura y guardado registran marcas de tiempo precisas y estadísticas (filas/columnas) directo en `logs/proyecto.log`, manteniendo los cuadernos `.ipynb` limpios y sin salidas de depuración innecesarias.
- **Manejo de Rutas con `pathlib`:** El proyecto resuelve la raíz de forma absoluta y dinámica. El código no se romperá si abres o trasladas los cuadernos a subcarpetas.

---

## 🚀 Guía de Uso del Proyecto

### 1. Clonar el repositorio e instalar dependencias

Asegúrate de tener `uv` instalado de forma global en tu máquina. Luego, dentro del directorio del proyecto, inicializa todo con un único comando:

```bash
uv sync
```

_Este comando leerá el archivo `pyproject.toml`, creará la carpeta `.venv` de forma instantánea y enlazará tu paquete `src` en modo editable._

### 2. Flujo de Trabajo con `uv`

- **Para añadir una nueva librería al análisis (ej. Scikit-Learn):**
  ```bash
  uv add scikit-learn
  ```
- **Para añadir herramientas exclusivas de desarrollo (ej. Linters o formatters):**
  ```bash
  uv add --dev ruff
  ```
- **Para ejecutar scripts directamente en la terminal sin activar el entorno:**
  ```bash
  uv run python src/procesar.py
  ```

### 3. Visualizar los Logs en Vivo en VS Code

Para monitorear el comportamiento del código en segundo plano mientras utilizas tus cuadernos:

1. Haz clic derecho sobre el archivo `logs/proyecto.log`.
2. Selecciona **Open to the Side** (Abrir a un lado).
3. Podrás observar los registros de auditoría añadirse en vivo cada vez que llames a funciones de carga de datos en tu Notebook.
