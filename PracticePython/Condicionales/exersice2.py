password = input("Escribe la contraseña: ")

re_password = input("Repite la contraseña: ")

if password.lower() == re_password.lower():
    print("Las contraseñas coinciden")
else:
    print("Las contraseñas NO coinciden...")