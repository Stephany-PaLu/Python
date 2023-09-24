#Crear un repositorio en Github que contenga dos archivos:
# 1. Lista de paquetes incluidos en su ambiente - Tienen la opción de hacerlo automáticamente con conda env export o manualmente

# 2. Un script que haga lo siguiente:

install.packages("reticulate")
library(reticulate)
use_condaenv("AmbienteTarea.yml")

# a. Cargue un paquete de su elección - Recuerden que debe estar disponible en su ambiente
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# b. Dos variables, una que contenga su nombre y la otra su edad


# c. Crear una oración que indique su nombre y su edad utilizando las dos variables creadas en el paso anterior


