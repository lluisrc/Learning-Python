# Esto es una búsqueda, no un recorrido
register_password = input("Introduce la contraseña: ")

acces_password = input("Introduce la contraseña para entrar: ")

while register_password != acces_password:
    print("No se ha introducido la contraseña correctamente...")
    acces_password = input("Introduce la contraseña de nuevo: ")

print("Acceso satisfactorio")