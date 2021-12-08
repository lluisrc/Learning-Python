# La tupla es una serie de elementos correlativos que no su pueden modificar

# Imprime por pantalla una posicion de la tupla
x = (1, 2, 3, 4, 5)
print(x[0])

# Si la tupla tiene un elemento, lo trata como string/int
y = (6)
print(type(y))

# Para conseguir que la tupla tenga un elemento utilizamos la ,
z = (7,)
print(type(z))

# Como no se puede modificar, lanza un error
# x[4] = 10

# Eliminar tupla
# del x
# print(x)

# Ejemplo tuplas dentro de una colección
locations = {
    (34.67432, 34.67434):"Tokyo",
    (36.43794, 37,35342):"New York"
}