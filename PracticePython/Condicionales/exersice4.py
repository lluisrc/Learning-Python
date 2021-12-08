numero = int(input("Escribe un numero: "))

operacion = numero%2 # El módulo(%) es el resto de una división

if operacion == 0:
    print("El numero es par")
else:
    print("El numero es impar")