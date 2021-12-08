horas = input("Cuantas horas has trabajado: ")
horas = int(horas)

saldo = int(input("Cual es tu saldo x hora? "))


total = saldo*horas

print("Te toca cobrar " + str(total) + " euros")