numero = int(input("Introduce un numero: "))

# i es el índice del for, se define como el primer parámetro del bucle
# El último -1 indica que le resta 1 a i
for i in range(numero, -1, -1):
    print(i, end=", ")