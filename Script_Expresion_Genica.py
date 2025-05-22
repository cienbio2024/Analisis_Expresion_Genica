# Paso 1: Importar las bibliotecas necesarias
import pandas as pd                  # Pandas permite manejar y analizar datos tabulares
import matplotlib.pyplot as plt      # matplotlib se usa para crear gráficos

# Paso 2: Subir el archivo desde tu computador (compatible con Colab y local)
import sys
if 'google.colab' in sys.modules:
	from google.colab import files
	uploaded = files.upload()           # Esto abrirá una ventana para que subas el archivo
	file_name = list(uploaded.keys())[0]
else:
	# Si no está en Colab, pedir el nombre del archivo o usar un diálogo estándar
	import tkinter as tk
	from tkinter import filedialog
	root = tk.Tk()
	root.withdraw()
	file_name = filedialog.askopenfilename(title="Selecciona el archivo Excel", filetypes=[("Excel files", "*.xlsx *.xls")])
	if not file_name:
		raise Exception("No se seleccionó ningún archivo.")

df = pd.read_excel(file_name) # Lee el archivo y lo guarda como una tabla en la variable 'df'
# Lee el archivo y lo guarda como una tabla en la variable 'df'

# Paso 4: Mostrar las primeras filas para verificar que se cargó correctamente
print("Vista previa de los datos:")
print(df.head())

# Paso 5: Calcular el promedio de expresión de cada gen
df["promedio"] = df[['Muestra_1', 'Muestra_2', 'Muestra_3']].mean(axis=1)
# ▸ Selecciona las columnas de las muestras
# ▸ Calcula el promedio fila por fila (axis=1)
# ▸ Crea una nueva columna llamada 'promedio' con ese valor

# Paso 6: Mostrar el DataFrame con la nueva columna
print("\nDatos con columna de promedio añadida:")
print(df)

# Paso 7: Crear un gráfico de barras con los valores promedios
plt.figure(figsize=(10, 5))                          # Define el tamaño del gráfico
plt.bar(df["Gen"], df["promedio"], color='skyblue')  # Crea barras: eje x = nombres de genes, eje y = promedio
plt.title("Expresión promedio por gen")              # Título del gráfico
plt.xlabel("Gen")                                    # Etiqueta del eje x
plt.ylabel("Expresión promedio")                     # Etiqueta del eje y
plt.xticks(rotation=45)                              # Gira etiquetas para mejor visibilidad
plt.tight_layout()                                   # Ajusta el diseño para que no se sobrepongan
plt.show()                                           # Muestra el gráfico
