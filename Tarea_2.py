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
Ecuador = "Ecuador"
Ecuador
Noruega = "Noruega"
Noruega

primer_año.loc['Ecuador']

# Filtrar datos para los dos países en el primer año

Ecuador_primer_año = datos_felicidad.loc['Ecuador']
Ecuador_primer_año

Noruega_primer_año = datos_felicidad.loc['Noruega']
Noruega_primer_año

# Filtrar datos para los dos países en el último año
datos_pais1_ultimo_anio = ultimo_anio[ultimo_anio['país'] == pais1]
datos_pais2_ultimo_anio = ultimo_anio[ultimo_anio['país'] == pais2]

# Obtener los valores de felicidad para los dos países en el primer año
felicidad_pais1_primer_anio = datos_pais1_primer_anio['felicidad'].values[0]
felicidad_pais2_primer_anio = datos_pais2_primer_anio['felicidad'].values[0]

# Obtener los valores de felicidad para los dos países en el último año
felicidad_pais1_ultimo_anio = datos_pais1_ultimo_anio['felicidad'].values[0]
felicidad_pais2_ultimo_anio = datos_pais2_ultimo_anio['felicidad'].values[0]

# Imprimir los valores de felicidad para comparación
print(f"Felicidad en {pais1} en el primer año: {felicidad_pais1_primer_anio}")
print(f"Felicidad en {pais2} en el primer año: {felicidad_pais2_primer_anio}")
print(f"Felicidad en {pais1} en el último año: {felicidad_pais1_ultimo_anio}")
print(f"Felicidad en {pais2} en el último año: {felicidad_pais2_ultimo_anio}")
Este código te permitirá comparar los valores de felicidad de dos países específicos con los valores a nivel mundial en el primer y último año reportado en tus datos. Asegúrate de reemplazar "País1" y "País2" con los nombres reales de los países que deseas analizar.






























