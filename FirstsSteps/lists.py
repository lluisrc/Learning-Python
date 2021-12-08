demo_list = [1, "hello", 1.34, True, [1,2,3]]
colors = ["red", "blue", "yellow", "red"]

numbers_list = list((1, 2, 3, 4))
# print(numbers_list)

# Crear una lista a partir de un rango
r = list(range(1, 10))
print(r)

# Que métodos podemos utilizar de la lista colors
print(dir(colors))

print(len(colors))
print(len(demo_list))

print(colors[1])
print(colors[-1])

# Está yellow en la lista colors (True or False)
print("yellow" in colors)

# Asigna un valor a una posición
print(colors)
colors[1] = "green"
print(colors)

# Añade un elemento a la lista
colors.append("violet")
print(colors)

# Usamos extend para añadir mas de un valor a la lista colors
# No se puede pasar por parámetro 2 elementos, así que se utiliza la tabla/tupla, que actúa como un solo elemento
colors.extend(["brown", "purple"])
colors.extend(("pink", "black"))
print(colors)

# Insertar un elemento en una posición específica
colors.insert(1, "violet")
print(colors)

# Para añadir un elemento en la última posición podemos usar el método len(), la posición len siempre es una mas que la última de la lista
# Para añadir un elemento mejor usar el método append()
colors.insert(len(colors), "white")
print(colors)

# Quitar el último elemeto de la lista
colors.pop()
print(colors)

# Quitar un elemento por posición
colors.pop(1)
print(colors)

# Quitar un elemento específico
colors.remove("green")
print(colors)

# Limpiar la lista
# colors.clear()
print(colors)


# Ordenar lista alfabéticamente
colors.sort()
print(colors)

# Ordenar lista alfabéticamente, reverso
colors.sort(reverse=True)
print(colors)

# Ver los índices de los elementos de una lista
print(colors.index("brown"))

# Cuenta cuantos elementos red hay en la lista
print(colors.count("red"))