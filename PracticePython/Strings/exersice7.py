# Del correo solo nos interesa la parte de antes del @, el truco está en conseguir la posicion del @ y seleccionar el rango que nos interesa.
correo = input("Introduzca una dirección de correo: ")

print(email[:email.find("@")] + "@ceu.es")

# Equivale a esto
# print(email[:5] + "@ceu.es")


