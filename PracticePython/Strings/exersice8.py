precio = input("Indica el precio del producto: ")

print("total " + precio[precio.find(".")+1:] + " centimos")
print("total " + precio[:precio.find(".")] + " euros")