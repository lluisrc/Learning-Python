cantidad = float(input("Introduce la cantidad a invertir: "))
interes = float(input("Introduce el interes anual: "))
anos = int(input("Introduce el numero de años: "))

for i in range(1, anos + 1):
    cantidad = cantidad * (1 + interes) # cantidad *= 1 + interes / 100 --> lo mutiplica y después lo asigna
    print(cantidad)