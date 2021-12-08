# Crea una lista adicional para meter las que han pasado... despues borra de la oraginal todas las que han padaso.

asignaturas = ["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"]
suspendidas = []

for i in asignaturas:
    nota = int(input("Introduce la nota de " + i + ": "))
    if nota < 5:
        suspendidas.append(i)

print("Tienes que repetir estas asignaturas: " + str(suspendidas))