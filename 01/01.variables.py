import math

# variables en minuscula y usar snakeCase

first_name = 'Joe'
last_name = 'Doe'
country = 'Argentina'
city = 'Tandil'
age = 30
is_married = False
skills = ['HTML', 'CSS', 'PYTHON']
person_info = {
    'firstname' : "Joe",
    'lastname' : 'Doe'
    }
promedio_secundario = 9.8

print(first_name, last_name)  # Se imprime concatenado

bool_variable = False
print(bool_variable)

convertir_a_string = str(age)
print(convertir_a_string)
print(type(convertir_a_string))
print(int(promedio_secundario))
print(float(promedio_secundario))
print(list(first_name))

#crear variables variables en una sola linea

primero, segundo, tercero, cuarto = 1, "Hola", False, 5

#Verificar todos los tipos de datos
print(type(first_name))
print(type(last_name))
print(type(country))
print(type(city))
print(type(age))
print(type(is_married))
print(type(skills))
print(type(person_info))
print(type(promedio_secundario))

#longitud del nombre
print(len(first_name))

#Comparar longitud de nombre y apellido
print("Longitud del nombre:",len(first_name), "y la longitud del apellido:",len(last_name))

#operaciones
primer_numero , segundo_numero= 5, 4
suma = primer_numero + segundo_numero
resta = primer_numero - segundo_numero
multiplciacion = primer_numero * segundo_numero
division = primer_numero/segundo_numero
modulo = segundo_numero%primer_numero
potencia = primer_numero**segundo_numero
floor_division = primer_numero//segundo_numero
print('Resultados... Suma:',suma,"Resta:",resta,"Multiplicacion:",multiplciacion,"Division:",division,"Modulo:",modulo,"Potencia:",potencia,"Floor:",floor_division)

#Si el radio de un circulo es 30
radio = 30
area = math.pi * radio ** 2
print("El area es de:",area)
circunferencia = 2 * math.pi * 2
print("La circunferencia es de:",circunferencia)
ingresar_radio = float(input("Ingresar radio del circulo en metros:"))
area_del_circulo = math.pi * ingresar_radio ** 2
print("El area del circulo es de:", area_del_circulo)

#Guardar en variables
first_name_1 = str(input("Ingrese su nombre:"))
last_name_1 = str(input("Ingrese su apellido:"))
country_1 = str(input("Ingrese su pais:"))
age_1 = int(input("Ingrese su edad:"))
print("Hola", first_name_1, last_name_1, ",usted tiene:", age_1, "y es de:", country_1)
