import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Acceder los datos de manera remota, es decir no bajándolos a su computadora.

datos_partidos= pd.read_csv('https://raw.githubusercontent.com/cienciadedatos/datos-de-miercoles/master/datos/2019/2019-04-10/partidos.txt',delimiter='\t')
datos_partidos
