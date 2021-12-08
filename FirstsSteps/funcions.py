# Función sencilla
def hello():
    print("Hola Mundo")

hello()
hello()
hello()

# Pasar parámetro a la función
def hello(name):
    print("Hola " + name)

hello("Lluis")
hello("Monica")

# Parámetro por defecto
def hello(name="Toni"):
    print("Hola " + name)

hello("Joan")
hello() # Al no pasar ningun parámetro a la funcion se utiliza la por defecto


def add(n1, n2):
    return n1 + n2
    
print(add(3, 5))