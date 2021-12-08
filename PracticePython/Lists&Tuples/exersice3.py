asignaturas = ["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"]
notas = []
control = 0

for i in asignaturas:
    print("Introduce la nota de " + i)
    nota = input("Introduce la nota de la asignatura: ")
    notas.append(nota)

for i in asignaturas:
    print("En la asignatura " + i + " has sacado " + notas[control])
    control += 1

# Utiliza un rango numerico para dar el valor a la i y que coincida bien con las listas
# for i in range(len(subjects)):
# print("En " + subjects[i] + " has sacado " + scores[i])
