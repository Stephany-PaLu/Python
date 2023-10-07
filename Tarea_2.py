import pandas as pd
import numpy as np
import glob as glob

#obtener los datos sobre felicidad

datos_felicidad = pd.read_csv('https://raw.githubusercontent.com/cienciadedatos/datos-de-miercoles/master/datos/2019/2019-08-07/felicidad.csv')

# Medida de tendencia central y dispersión de la felicidad a nivel mundial para el primer y último año 
# incluido en el set de datos. Pueden escoger cualquier medida, por ejemplo, promedio y desviación estándar.

import pandas as pd

# Filtrar datos para el primer año
primer_año = datos_felicidad[datos_felicidad['anio'] == datos_felicidad['anio'].min()]

# Filtrar datos para el último año
ultimo_año = datos_felicidad[datos_felicidad['anio'] == datos_felicidad['anio'].max()]

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


























