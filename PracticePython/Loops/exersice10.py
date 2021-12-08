# Es una busqueda xq busca un numero que se pueda dividir, en el momento en que encuentra uno, para...

numero = int(input("Introduce un número entero positivo mayor que 2: "))
i = 2
while numero % i != 0:
    i += 1
if i == numero:
    print(str(numero) + " es primo")
else:
    print(str(numero) + " no es primo") 




# numero = int(input("Introduce un numero: "))
# primo = 0

# for i in range(2,numero):
#     if numero % i == 0:
#         primo = primo+1

# if primo == 0:
#     print("El numero SI es primo")
# else:
#     print("El numero NO es primo")