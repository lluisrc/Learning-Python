fecha = input("Pon una fecha: ")

# Opción 1
print("Día " + fecha[0:2])
print("Mes " + fecha[3:5])
print("Año " + fecha[6:10])


# Opción 2
fecha = input("Escribe la fecha de hoy: ")

print("El día es: " + fecha[:fecha.find("/")])

mesano = fecha[fecha.find("/")+1:]

print("El mes es: " + mesano[:mesano.find("/")])
print("El año es: " + mesano[mesano.find("/")+1:])


# Opción 2 (dividir en subgrupos)