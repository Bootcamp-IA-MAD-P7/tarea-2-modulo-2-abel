<div align="center">
    <h1>Proyecto de Análisis de Datos Modular <br/>+ Regresión Lineal Simple</h1>
    <h3>Dataset: Salary Dataset — Predicción de Salario por Años de Experiencia</h3>
</div>

IR A: [ Desarrollo de la tarea: 1 Parte teórica](#-fundamentos-de-regresión)

[DATASET URL: Salary_dataset.csv](https://docs.google.com/spreadsheets/d/e/2PACX-1vQU0SIALScXx8VXDX7yKNKWWPKE1YjFlWc6VTEVSN45CklWWf-uWmprQIyLtoPDA18tX9cFDr-aQ9S6/pubhtml)

## 📊 Descripción del Proyecto


Este proyecto implementa una estructura modular y moderna para el análisis estadístico y modelado de datos (EDA). El objetivo principal es estructurar un flujo de trabajo reproducible que incluye la limpieza de datos, análisis exploratorio e implementación de una **regresión lineal simple** para análisis predictivo.

Todo el ecosistema se administra mediante **uv** como gestor de paquetes de alto rendimiento, **Jupyter Notebooks** embebidos en **VS Code**, y un sistema de auditoría mediante logs automatizados y aislados.

---

## 🛠️ Tecnologías Utilizadas

| Tecnología                                                                                      | Propósito                                              |
| :---------------------------------------------------------------------------------------------- | :----------------------------------------------------- |
| <img src="https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white">         | Lenguaje de programación principal                     |
| <img src="https://img.shields.io/badge/UV-Package%20Manager-E95F9B">                            | Gestor de paquetes y entornos de ultra-alta velocidad  |
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

---

# 📊 Fundamentos de Regresión

### 1. ¿Qué es la regresión y cuál es su propósito en el Machine Learning? ¿En qué se diferencia de otros tipos de modelos supervisados como la clasificación?

- **Propósito:** La regresión es una técnica de aprendizaje supervisado cuyo objetivo es modelar la relación entre variables para **predecir un valor numérico continuo** (como el salario, el precio de una casa o la temperatura).

- **Diferencia con la Clasificación:** Aunque ambos son modelos supervisados (usan datos etiquetados), la diferencia radica en la naturaleza de la variable de salida (Y):
  - **Regresión:** Predice un número infinito de valores posibles en una escala continua (ej. un salario de \$45,500.50).
  - **Clasificación:** Predice una etiqueta o categoría discreta de un conjunto finito de opciones (ej. "Aprobar" / "Reprobar", o "Spam" / "No Spam").

---

### 2. ¿Qué es la Regresión Lineal Simple y qué representa la ecuación ŷ = β0 + β1 · X? Explica qué significan β0 (intercepto) y β1 (pendiente) y cómo interpretarlos en un contexto real.

La Regresión Lineal Simple busca modelar la relación entre una única variable independiente (X) y una variable dependiente (Y) trazando una línea recta óptima a través de los datos.

- **ŷ:** Es el valor estimado o predicho por el modelo.

- **β0 (Intercepto o sesgo):** Representa el valor esperado de Y cuando X es igual a cero.
  - _Contexto real:_ En el dataset de salarios, si X son los años de experiencia, β0 sería el sueldo base que recibe un empleado recién contratado con cero años de experiencia.

- **β1 (Pendiente o coeficiente):** Representa el cambio promedio en Y por cada incremento de una unidad en X.
  - _Contexto real:_ Si β1 = 5000, significa que por cada año adicional de experiencia (X), el salario del empleado (Y) aumentará en promedio \$5,000.

---

### 3. ¿Cuáles son los supuestos de la Regresión Lineal? Describe los supuestos principales y por qué es importante verificarlos.

Para que las predicciones y las inferencias estadísticas de una regresión lineal sean válidas y confiables, se deben cumplir cuatro supuestos fundamentales sobre los datos y sus errores:

1. **Linealidad:** La relación entre la variable independiente (X) y la variable dependiente (Y) debe ser esencialmente una línea recta.
2. **Homocedasticidad:** La varianza de los errores (residuos) debe ser constante a lo largo de todos los niveles de la variable independiente. Si los errores se vuelven más grandes a medida que X aumenta (forma de cono), hay _heterocedasticidad_.
3. **Independencia de errores (No autocorrelación):** Los residuos de una observación no deben estar correlacionados con los de otra. Esto es crítico en datos que siguen un orden temporal.
4. **Normalidad de residuos:** Los errores del modelo deben distribuirse siguiendo una distribución normal (campana de Gauss) centrada en cero.

- **Importancia de verificarlos:** Si estos supuestos se violan, las estimaciones de los coeficientes pueden ser engañosas, los intervalos de confianza serán incorrectos y el modelo perderá su capacidad predictiva real en datos nuevos.

---

### 4. ¿Qué es la función de coste (Loss Function) en regresión? Explica el MSE y el MAE. ¿Cuál es la diferencia y cuándo preferirías usar uno u otro?

- **Función de Coste:** Es una fórmula matemática que mide qué tan "equivocado" está el modelo. Calcula la penalización o distancia acumulada entre las predicciones del algoritmo (ŷ) y los valores reales (y). El objetivo del entrenamiento es minimizar este valor.

- **Error Cuadrático Medio (MSE):** Promedia los errores elevados al cuadrado. Al elevarlos, **penaliza severamente los errores grandes (outliers)**.

- **Error Absoluto Medio (MAE):** Promedia los valores absolutos de los errores. Trata a todas las desviaciones de forma lineal.

- **Diferencias y Cuándo Usar Cada Uno:**
  - **Prefieres MSE** cuando los errores grandes son catastróficos para tu negocio y quieres que el modelo haga todo lo posible por evitarlos.
  - **Prefieres MAE** cuando tus datos contienen valores atípicos (outliers) extremos que no quieres que distorsionen o "jalen" la tendencia general del modelo, ya que el MAE es mucho más robusto frente a ruidos.

---

### 5. ¿Qué significa dividir los datos en train y test? ¿Por qué es necesario? ¿Qué problema evitamos al no evaluar el modelo con los mismos datos con los que lo entrenamos?

- **¿Qué significa?:** Consiste en separar de forma aleatoria el conjunto de datos original en dos bloques:
  1. **Train (Entrenamiento):** Generalmente el 70% u 80% de los datos. Se usa para que el modelo aprenda los patrones y calcule los coeficientes (β0, β1).
  2. **Test (Prueba):** El 20% o 30% restante. Se guarda bajo llave y se usa exclusivamente para evaluar el rendimiento del modelo al final.

- **¿Por qué es necesario?:** En la práctica, no nos interesa qué tan bien recuerda el modelo el pasado, sino qué tan bien puede **generalizar** ante datos futuros que nunca ha visto.

- **Problema que evitamos:** Evitamos el autoengaño y el **Overfitting (Sobreajuste)**. Si evaluamos el modelo con los mismos datos de entrenamiento, un algoritmo podría simplemente "memorizar" el ruido y las anomalías de esos datos específicos, obteniendo una puntuación perfecta falsa que fallará rotundamente en el mundo real.

---

### 6. ¿Qué métricas se usan para evaluar un modelo de regresión? Investiga y explica con sus fórmulas:

- **R2 (Coeficiente de determinación):** Mide la proporción de la varianza en la variable dependiente que es explicable por la variable independiente. Va de 0 a 1 (o 0% a 100%).
  - _Fórmula:_ `R² = 1 - ( ∑(y_i - ŷ_i)² / ∑(y_i - y_promedio)² )`

- **MSE (Mean Squared Error):** Mide el promedio de los errores al cuadrado. Es útil para la optimización matemática del algoritmo.
  - _Fórmula:_ `MSE = (1 / n) * ∑(y_i - ŷ_i)²`

- **RMSE (Root Mean Squared Error):** Es la raíz cuadrada del MSE. Devuelve la métrica a las **mismas unidades originales** que la variable Y (ej. dólares, metros), haciéndola mucho más interpretable.
  - _Fórmula:_ `RMSE = √[ (1 / n) * ∑(y_i - ŷ_i)² ]`

- **MAE (Mean Absolute Error):** Mide la magnitud promedio de los errores en términos absolutos sin importar su dirección.
  - _Fórmula:_ `MAE = (1 / n) * ∑|y_i - ŷ_i|`

---

### 7. ¿Qué son los residuos y para qué sirve analizarlos? ¿Qué indica un residuo cercano a 0? ¿Qué patrón en los residuos revelaría que el modelo no es adecuado?

- **¿Qué son?:** El residuo es la diferencia exacta entre el valor real observado y el valor predicho por la línea de regresión (e = y - ŷ).

- **Análisis de Residuos:** Sirve como una herramienta de diagnóstico para verificar si se cumplen los supuestos de la regresión lineal.

- **Residuo cercano a 0:** Indica que la predicción del modelo fue sumamente precisa para esa observación en particular.

- **Patrones que revelan fallas:**
  - Si los residuos forman una **curva o parábola** (forma de U), revela que la relación real es no lineal y que una línea recta no es adecuada.
  - Si los residuos forman un **embudo o cono** (se esparcen más en un extremo), revela una violación al supuesto de homocedasticidad.

---

### 8. ¿Qué es el overfitting y cómo se detecta comparando R2 en train vs. test?

- **Overfitting (Sobreajuste):** Ocurre cuando el modelo aprende tan detalladamente los datos de entrenamiento que termina memorizando el ruido, las fluctuaciones aleatorias y los errores muestrales.

- **Detección con R2:** Se identifica analizando la brecha de rendimiento entre conjuntos:
  - El modelo presenta Overfitting si el **R2 en Train es muy alto** (ej. 95%), pero al evaluar el **R2 en Test el rendimiento cae drásticamente** (ej. 60%). Esto demuestra que el modelo memorizó pero perdió la capacidad de generalizar.

---

### 9. ¿Qué es la validación cruzada (cross-validation) y qué ventaja ofrece frente a una sola división train/test?

- **¿Qué es?:** Es una técnica avanzada de evaluación donde los datos se dividen en K partes iguales (llamadas _folds_). El modelo se entrena K veces; en cada iteración, se utiliza una parte distinta como conjunto de prueba (Test) y las K-1 partes restantes como conjunto de entrenamiento (Train). Al final, se promedian los resultados de las K evaluaciones.

- **Ventajas frente a train/test único:**
  - **Reduce la dependencia del azar:** Evita que una división "afortunada" o "desafortunada" de los datos altere artificialmente las métricas del modelo.
  - **Aprovechamiento de datos:** Garantiza que cada uno de los registros del dataset sea utilizado tanto para entrenar como para probar en algún momento, ofreciendo una estimación mucho más robusta y realista del rendimiento del modelo en producción.
