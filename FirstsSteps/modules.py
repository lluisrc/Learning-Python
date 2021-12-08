# Existen 3 tipos de módulos: Módulos de Python, Módulos de terceros y Módulos propios
# Los módulos de Python y los módulos propios se pueden importar directamente
# Los módulos de terceros necesitan ser instalados mediante el comando pip.
# Después existe los modulos internos que son los que utiliza python para sus funciones propias ya definidas

# Importar el modulo datatime
import datetime

print(datetime.date.today())

print(datetime.timedelta(minutes = 70))


# Importar un submodulo
from datetime import timedelta, date

print(timedelta(minutes = 260))
print(date.today())


# Crear mi propio modulo, lo llamo desde mi archivo mimodulo.py
import mimodulo

mimodulo.add(4, 5)
mimodulo.substract(10, 8)

# Importar mis submodulos
from mimodulo import add, substract
add(6, 7)
substract(36, 10)


# Importar un módulo de terceros, Colorama

# Ejecutamos a través de la línea de comandos: pip install colorama
from colorama import Fore, Style, init

init(convert=True)
print(Fore.RED + "Hello world")




# En esta url puedes encontrar modulos de terceros: https://pypi.org/