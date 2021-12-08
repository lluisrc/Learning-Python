print("PANADERIA PEPITO")
precio_noraml = 3.49
descuento = 0.60
barras = float(input("Cuantas barras de pan de ayer se han vendido? "))

total = barras*precio_noraml
total_rebajado = (1-descuento)*total

print("El precio normal es de " + str(total) + ", se aplica el 60% " + str(total*descuento) + " dando como resultado total " + str(total_rebajado))

