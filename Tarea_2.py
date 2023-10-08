import pandas as pd
import numpy as np
import glob as glob
import os

#obtener los datos sobre felicidad

datos_felicidad = pd.read_csv('https://raw.githubusercontent.com/cienciadedatos/datos-de-miercoles/master/datos/2019/2019-08-07/felicidad.csv', index_col="pais")
datos_felicidad
# Medida de tendencia central y dispersión de la felicidad a nivel mundial para el primer y último año 
# incluido en el set de datos. Pueden escoger cualquier medida, por ejemplo, promedio y desviación estándar.

# Filtrar datos para el primer año
primer_año = datos_felicidad[datos_felicidad['anio'] == datos_felicidad['anio'].min()]
primer_año

# Filtrar datos para el último año
ultimo_año = datos_felicidad[datos_felicidad['anio'] == datos_felicidad['anio'].max()]
ultimo_año

# Calcular promedio y desviación estándar para el primer año
promedio_primer_año = primer_año['escalera_vida'].mean()
promedio_primer_año

desviacion_primer_año = primer_año['escalera_vida'].std()
desviacion_primer_año

# Calcular promedio y desviación estándar para el último año
promedio_ultimo_año = ultimo_año['escalera_vida'].mean()
promedio_ultimo_año


desviacion_ultimo_año = ultimo_año['escalera_vida'].std()
desviacion_ultimo_año


# Elegir dos países 
Autralia
Canadá

primer_año.loc['Brasil']

# Filtrar datos para los dos países en el primer año

Australia_primer_año = primer_año.loc['Australia']
Australia_primer_año

Canadá_primer_año = primer_año.loc['Canadá']
Canadá_primer_año

# Filtrar datos para los dos países en el último año
Australia_ultimo_año = ultimo_año.loc['Australia']
Australia_ultimo_año

Canadá_ultimo_año = ultimo_año.loc['Canadá']
Canadá_ultimo_año

# Obtener los valores de felicidad para los dos países en el primer año
felicidad_Australia_1año = Australia_primer_año.loc['escalera_vida']

felicidad_Canada_1año = Canadá_primer_año.loc['escalera_vida']

# Obtener los valores de felicidad para los dos países en el último año
felicidad_Austra_ultimo_año = Australia_ultimo_año.loc['escalera_vida']

felicidad_Canada_ultimo_año = Canadá_ultimo_año.loc['escalera_vida']


# Imprimir los valores de felicidad para comparación
print(f"Felicidad en {pais1} en el primer año: {felicidad_pais1_primer_anio}")
print(f"Felicidad en {pais2} en el primer año: {felicidad_pais2_primer_anio}")
print(f"Felicidad en {pais1} en el último año: {felicidad_pais1_ultimo_anio}")
print(f"Felicidad en {pais2} en el último año: {felicidad_pais2_ultimo_anio}")
Este código te permitirá comparar los valores de felicidad de dos países específicos con los valores a nivel mundial en el primer y último año reportado en tus datos. Asegúrate de reemplazar "País1" y "País2" con los nombres reales de los países que deseas analizar.






























