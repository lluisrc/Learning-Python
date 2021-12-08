frase = input("Introduce una frase: ")
letra = input("Introduce una letra: ")
count = 0

for i in frase:
    if i == letra:
        count += 1

print("Se ha encontrado un total de " + str(count) + (" coindicencias"))
# print("La letra '%s' aparece %2i veces en la frase '%s'." % (letra, contador, frase))