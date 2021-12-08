peso = float(input("Dame tu peso: "))
altura = float(input("Dame tu altura: "))
imc = round(peso/altura**2,2)

print("Tu masa corporal es: " + str(imc))