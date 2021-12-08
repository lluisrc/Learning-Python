pizza = input("Vegetariano o normal: ")

if pizza.lower() == "vegetariano":
    print("PIMIENTO O TOFU")
    ingrediente = input("Elige un ingrediente: ")
    print("La piza elegida es " + pizza + " y el ingrediente elegido es " + ingrediente)

elif pizza.lower() == "normal":
    print("PEPERONI JAMON O SALMON")
    ingrediente = input("Elige un ingrediente: ")
    print("La piza elegida es " + pizza + " y el ingrediente elegido es " + ingrediente)

else:
    print("Respuesta no aceptada")


