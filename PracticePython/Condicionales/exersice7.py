renta = int(input("Introduce tu renta anual: "))

if renta < 10000:
    print("Te toca pagar el 5%")
elif renta >= 10000 and renta < 20000:
    print("Te toca pagar el 15%")
elif renta >= 20000 and renta < 35000:
    print("Te toca pagar el 20%")
elif renta >= 35000 and renta < 60000:
    print("Te toca pagar el 30%")
elif renta >= 60000:
    print("Te toca pagar el 45%")
    print("Equivale a " + str(int(renta) * 0.45) + " obteniendo un ingreso total de " + str(int(renta * (1-0.45))))