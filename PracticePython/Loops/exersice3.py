numero = int(input("Introduce un número: "))

for i in range(numero + 1):
    if numero % 2 == 1:
        print(numero)

    numero = numero - 1


    # for i in range(1, numero+1, 2):