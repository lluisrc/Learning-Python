peso_payaso = 112
peso_muñeca = 75

no_payasos = input("Introduce el numero de payasos a enviar: ")
no_muñecas = input("Introduce el numero de muñecas a enviar: ")

total = int(no_payasos)*peso_payaso + int(no_muñecas)*peso_muñeca

print("El paquete pesa un total de " + str(total))