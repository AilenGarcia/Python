#Operadores aritmeticos
print(3+4) # igual con + - * / % **(exponente) etc
print(10 // 3) #floor division (Siempre devolvera un entero)
print(2 ** 3 + 3 - 7 / 1 // 4)

print("Hola " + "Python") #El + tambien lo concatena. Tiene muchas opciones, no solo matematicas.
#print("Hola" + 5) devuelve error.
print("Hola " + str(5)) #Esta vez si lo permite, porque el 5 esta como String
print("Repetir " * 2)

#Operadores comparativos
print(3>4) #Tambien se podria con ==, !=, > = etc
print(3<4)
print(3 > 4 != 2)
print("Hola" > "Python")
print(len("Hola") > len("Python"))
print(len("Hola") < len("Python"))
print("aaaa" >= "abaa") #ordena alfabeticamente
print(len("aaaa") >= len("abaa")) #cuenta caracteres

# Operadores logicos
print(3>4 and "Hola" > "Python")
print(3>4 or "Hola" > "Python")
print(3<4 and "Hola" < "Python")
print(3<4 or "Hola" < "Python")
print(not (3 > 4))