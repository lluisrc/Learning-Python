n = int(input("Dame un numero: "))

m = int(input("Dame otro numero: "))

resultado = n/m
resultado = int(resultado)

resto = n%m

print("La division " + str(n) + " entre " + str(m) + " dá como cuociente " + str(resultado) + " y resto " + str(resto))