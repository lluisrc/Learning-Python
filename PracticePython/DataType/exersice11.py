print("BIENVENDIO A MI BANCO")

balance_actual = int(input("Cuanto dinero deseas depositar: "))
interes = 4/100 # = 0.04

primer_ano = balance_actual * interes + balance_actual
print("El primer año has ahorrado " + str(round(balance_actual * interes, 2)) + " con un total de " + str(round(primer_ano, 2)))

segundo_ano = primer_ano * interes + primer_ano
print("El primer año has ahorrado " + str(round(primer_ano * interes, 2)) + " con un total de " + str(round(segundo_ano, 2)))

tercer_ano = segundo_ano * interes + segundo_ano
print("El primer año has ahorrado " + str(round(segundo_ano * interes, 2)) + " con un total de " + str(round(tercer_ano, 2)))
