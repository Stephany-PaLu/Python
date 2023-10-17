import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Acceder los datos de manera remota, es decir no bajándolos a su computadora.

datos_partidos= pd.read_csv('https://raw.githubusercontent.com/cienciadedatos/datos-de-miercoles/master/datos/2019/2019-04-10/partidos.txt',delimiter='\t', index_col=)
datos_partidos

# 2. Crear dos gráficos en el que comparen a al menos dos países diferentes. Si quieren incluir a más países pueden hacerlo.

equipos = datos_partidos[(datos_partidos.equipo_1 == 'Argentina') | (datos_partidos.equipo_1 == 'Brasil')]
equipos
