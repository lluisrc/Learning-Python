# bucle for
foods = ["manzana", "pan", "leche", "huevos", "arroz", "espaguetis"]

for food in foods:
    if food == "pan":
        print("tienes que comprar esto: ")
        continue # sal de la sentencia y pasa al siguiente elemento
    if food == "huevos":
        break # sal de la sentencia y sal del bucle
    print(food)

# El primer parámetro enta incluido en el rango, el segundo no  (1-7)
for number in range(1, 8):
    print(number)


for letra in "hello":
        print(letra)


# bucle while
count = 4

while count <= 10:
    print(count)
    count = count + 1