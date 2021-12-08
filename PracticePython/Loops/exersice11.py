word = input("Introduce una palabra: ")

# i coje el primer valor del recorrido
# En este caso el -1 es xq len coge el primer char como 1
for i in range(len(word)-1, -1, -1):
    print(word[i])