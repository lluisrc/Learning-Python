word = input("Introduce una palabra: ")
vocals = ['a', 'e', 'i', 'o', 'u']
for vocal in vocals: 
    times = 0
    for letter in word: 
        if letter == vocal:
            times += 1
    print("La vocal " + vocal + " aparece " + str(times) + " veces")



# palabra = input("Introduce una palabra: ")
# a = 0
# e = 0
# i = 0
# o = 0
# u = 0

# for j in palabra:
#     if j == "a":
#         a += 1
#     if j == "e":
#         e += 1
#     if j == "i":
#         i += 1
#     if j == "o":
#         o += 1
#     if j == "u":
#         u += 1

# print("A :" + str(a))
# print("E :" + str(e))
# print("I :" + str(i))
# print("O :" + str(o))
# print("U :" + str(u))
    