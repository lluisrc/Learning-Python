# Set define una colección que no tiene índice
colors = {"Red", "Green", "Blue"}
print(type(colors))

#Existe un elemente dentro de la colección (True or False)
print("Red" in colors)

# Añadir un elemento a la colección
colors.add("Violet")
print(colors)

# Quitar un elemento de la colección
colors.remove("Red")
print(colors)

# Quitar todos los elementos de la colección
colors.clear()
print(colors)

# Eliminar la colección
# del colors
# print(colors)