'''
Created on 10 oct 2022

@author: Kike Rueda
'''
#BOLETIN 6#
'''
print("EJ1")
Design a program to show all numbers between 1 and 100. If the number is a
multiple of 7 you should show the message "The number xx is a multiple of 7". If the
number is a multiple of 13 you should show the message "The number xx is a
multiple of 13". If the number is a multiple of 7 and 13 you should show both
messages.'''
'''
num = int(input("Elige un numero (1-100): "))

while num<1 or num>100:
    num = int(input("Elige un numero (1-100): "))
   
    if num%7==0 and num%13==0:
        print(f"{num} es multiplo de 7 y de 13")
    elif num%7==0:
        print(f"{num} es multiplo de 7")
    elif num%13==0:
        print(f"{num} es multiplo de 13")
 '''
print("Ejercicio 2")
numero=int(input("Ingrese un número entre 0 y 10: "))
while numero<0 or numero>10:
    print("El número está fuera de los límites")
    numero=int(input("Ingrese un número entre 0 y 10: "))   
for i in range(11):
    total=numero*i
    print(f"{numero}*{i}={total}")
'''
print("Ejercicio 3")

cantidad= int(input("¿Cuántos números desea ingresar?"))

while cantidad<=0:
    cantidad= int(input("El valor no es correcto.¿Cuántos números desea ingresar?"))
    
for i in range(cantidad):
    numero=int(input("Ingrese un número mayor que 0: "))
    
    while numero<=0:
        numero=int(input("El numero no es valido. Introduce un número mayor que 0: "))
    if numero%2==0:
        print(f"El numero {numero} es par")
    else:
        print(f"El numero {numero} es impar")
''''''   
print("Ejercicio 4")
numero=int(input("Introduce un numero mayor que 0: "))
while numero<=0:
    numero=int(input("El numero es incorrecto, intentelo de nuevo: "))
suma=0
for i in range(1,numero):
    suma= suma+i
print(f"La suma de los {numero} primeros numeros es {suma}")
''''''
print("Ejercicio 5")
numero=int(input("Ingrese un numero (negativo para terminar):"))
total=0

while numero>0:
    total+=1
    numero=int(input("Ingrese un numero (negativo para terminar):"))
    print(total)
print(f"Ha ingresado {total} numeros positivos")
''''''   
print("Ejercicio 6")
numA=int(input("Ingrese un numero: "))
numB=int(input("Ingrese el segundo numero: "))
total=0

for i in range(numA):
    total+=numB

print(total)
''''''
print("Ejercicio 7")

cantidad=int(input("¿Cuántos números desea ingresar?"))
while cantidad<=0:
    print("La cantidad no es válida, debe ser mayor a 0")
    cantidad=int(input("¿Cuántos números desea ingresar?"))
    
suma=0
    
for i in range(cantidad):  
    numero=int(input("Ingrese un número mayor que 0: "))  
    while numero<=0:
        print("El numero no es válido, debe ser mayor a 0")
        numero=int(input("Ingrese un número mayor que 0: "))
    
    suma+=numero
media=suma/cantidad
print(f"La media es -->{media}")   
    
    



  

''''''
print("Ejercicio 8")
Diseñe un programa que solicite un conjunto de números. Después de ingresar cada número, el
El programa debe preguntar "¿Desea ingresar más números (S/N)?". Si la respuesta es "S"
el programa pide otros números. Cuando el usuario termine de ingresar todos los números,
el programa debe decir cuál es el más pequeño. Los mensajes son los siguientes:
“Ingrese un número:”
“¿Quieres ingresar más números (S/N)?”
“El número más pequeño es XX”''''''

num=int(input("Introduzca el primer numero: "))
peque=num

pregunta=(input("¿Desea ingresar más números? (S/N)"))

while pregunta.upper()=="S":
    num=int(input("Introduzca el siguiente numero: "))
    
    pregunta=(input("¿Desea ingresar más números? (S/N)"))
    
    if num<peque:
        peque=num
print(f"El numero mas pequeño es {peque}")

print("Ejercicio 9")
    
''''''Diseñe un programa que lea un número entero positivo mayor que 0 y diga si
es un "número perfecto". Un número es perfecto si es igual a la suma de todos sus divisores.
Los mensajes son los siguientes:
“Ingrese un número entero positivo mayor que 0:”
“El número no es válido, inténtalo de nuevo.”
“El número es perfecto”.
“El número no es perfecto”.
''''''
numero=int(input("Introduce un numero entero positivo mayor que 0: "))

while numero<=0:
    numero=int(input("El número no es válido, inténtalo de nuevo: "))
    
sumaDivisores=0

for i in range(1,numero):
    print(i)
    if numero%i==0:
        sumaDivisores= sumaDivisores+i
if sumaDivisores==numero:
    print("El número es perfecto")
else:
    print("El número no es perfecto")

    


print("Ejercicio 10")

#numero= int(input("Introduzca un numero entero positivo"))
numero=5
total=1
for i in range(1,numero+1):
    total= total*i
print(total)
'''