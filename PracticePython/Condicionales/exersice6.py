nombre = input("Introduce tu nombre: ")
sexo = input("Introduce tu sexo: ")

if (nombre.lower()[0] <= "m" and sexo.lower() == "mujer") or (nombre.lower()[0] >= "n" and sexo.lower() == "hombre"):
    print("Perteneces al grupo A")
else:
    print("Perteneces al grupo B")