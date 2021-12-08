loteria = []

for i in range(6):
    numero = input("Introduce el numero " + str(i+1) + " de la lotería: ")
    loteria.append(numero)

loteria.sort()
print(loteria)