#import  math
# Declare your age as integer variable
my_age = 24

# Declare your height as a float variable
my_height = 1.69

# Declare a variable that store a complex number
complex_number = 3 + 4j

# Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
""""
print("Vamos a averiguar el area de un triangulo")
base = float(input("Ingrese la base del triangulo: "))
height = float(input("Ingrese la altura del triangulo: "))
area = 0.5 * base * height
print("El area es de: " + str(area))
"""
# Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
""""
print("Vamos a calcular el perimetro de un triangulo")
a=float(input("Ingrese cuanto mide el primer lado: "))
b=float(input("Ingrese cuanto mide el segundo lado: "))
c=float(input("Ingrese cuanto mide el tercero lado: "))
perimeter = a +b +c
print("El perimetro es:", str(perimeter))
"""
#Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
"""
print("Vamos a calcular el area y perimetro de un rectangulo")
length = float(input("Ingrese el largo: "))
width = float(input("Ingrese el ancho:"))
area_rectangle = length * width
perimeter_rectangule = 2 * area_rectangle
print("El area es de:", str(area_rectangle), "y el perimetro es de:", str(perimeter_rectangule))
"""
#Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
"""
print("Vamos a calcular el area y circunferencia de un circulo")
radius = float(input("Ingrese el radio:"))
area_circle = math.pi * radius * radius
circumference = 2 * math.pi * radius
print("El area es de: " + str(area_circle) + " y la circunferencia es de: " + str(circumference))
"""
#Calculate the slope, x-intercept and y-intercept of y = 2x -2
"""
equation = "y = 2x - 2"
slope = 2
x_intercept = 1
y_intercept = -2

print("Ecuación:", equation)
print("Pendiente:", slope)
print("Intercepción en el eje x:", x_intercept)
print("Intercepción en el eje y:", y_intercept)
"""
#Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
"""
x1, y1 = 2, 2
x2, y2 = 6, 10
slope_2  = (y2 -y1)/(x2 -x1)
distance_2 = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("Pendiente:", slope_2)
print("Distancia Euclidiana:", distance_2)
"""
#Compare the slopes in tasks 8 and 9.
"""
print(slope > slope_2)
print(slope == slope_2)
"""
#Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
"""
x= 2
y = x**2 + 6*x + 9
print(y)
x = (-3)
y = x**2 + 6*x + 9
print(y)
"""
#Find the length of 'python' and 'dragon' and make a falsy comparison statement.
"""
python = "python"
dragon = "dragon"
print(len(python) > len(dragon))
#print(len(python) == len(dragon))
"""
#Use and operator to check if 'on' is found in both 'python' and 'dragon'
#There is no 'on' in both dragon and python
"""
print ('on' in python)
print('on' in dragon)
print (not 'on' in python)
print(not 'on' in dragon)
"""
#I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
"""
sentence = "I hope this course is not full of jargon"
print('jargon' in sentence)
"""

#Find the length of the text python and convert the value to float and convert it to string
length_python = len("python")
length_python_float = float(length_python)
length_python_str = str(length_python)
#Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
"""
consulta = int(input("Cual numero quiere comprobar si par? "))
is_even = bool((consulta % 2) == 0)
print(is_even)
"""
#Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
"""
operacion = 7 // 3
is_equal = bool(operacion == int(2.7))
print(is_equal)
"""
#Check if type of '10' is equal to type of 10
"""
print(type('10') == type(10))
"""
#Check if int('9.8') is equal to 10
"""
number = int('9.8')
print(number == 10)
"""
#Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
"""
hours = float(input("Ingrese la cantidad de horas: "))
rate_per_hour = float(input("Ingrese el salario por hora: "))
total = hours * rate_per_hour
print("El salario del dia es de: " + str(total))
"""
#Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
"""
years = int(input("Ingrese el año que quiera saber en segundos: "))
seconds_per_year = 365 * 24 * 60 * 60
total_seconds = years * seconds_per_year
print(total_seconds)
"""
#Write a Python script that displays the following table
"""
print("1 1 1 1 1")
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125")
"""