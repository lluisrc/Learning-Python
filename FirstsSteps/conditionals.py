# Condicionales if - elif - else
x = 20

if x < 20:
    print("el valor x es menor que 20")
elif x > 20:
    print("el valor x es mayor que 20")
else:
    print("el valor x es igual a 20")



# Condicionales anidados
name = "Lluis"
lastname = "Pujol"

if name == "Lluis":
    print("Eres Lluis")
    if lastname == "Roca":
        print("Eres Lluis Roca")
    else:
        print("No te apellidas Roca")
else:
    print("No eres Lluis")
    

# Condicionales con operadores lógicos
y = 5

if y > 0 and y < 10:
    print("Soy un numero entre 0 y 10")

else:
    print("No soy un número entre 0 y 10")