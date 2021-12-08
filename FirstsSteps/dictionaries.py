product = {
    "name":"book",
    "quantity":3,
    "prince":4.99
    }

person = {
    "first_name":"lluis",
    "last_name":"roca"
}

print(type(product))

# Los métodos que podemos
print(type(product))

# Obtener solo las llaves
print(person.keys())

# Obtener solo los valores
print(person.items())

# Eliminar diccionario
# del person
# print(person)

person.clear()
print(person)

# Los diccionarios se pueden agrupar en listas
products = [
    {
    "name":"book",
    "quantity":3,
    "prince":4.99
    },
    {
    "name":"laptop",
    "quantity":4,
    "prince":6.99
    },
    {
    "name":"monitor",
    "quantity":2,
    "prince":9.99
    }
]

print(products)