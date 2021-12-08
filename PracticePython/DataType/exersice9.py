cantidad = int(input("Inserte la cantidad a invertir: "))
interes = int(input("Inserte el interés anual: "))
anos = int(input("Inserte el numero de años: "))

total = (cantidad * (interes/100)) * anos


print("El capital obtenido es: " + str(total))