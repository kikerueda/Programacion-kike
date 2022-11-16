'''
Created on 26 sept 2022
Enrique Rueda DAW
'''
 #    BOLETIN 3   #
'''
print("(Ejercicio: 1)")
numero= int(input("Introduzca un numero "))
if numero%2==0:
    print("El número",numero,"es par")
else:
    print("El número",numero,"impar")
''''''   
print("(Ejercicio: 2)")
num1 = int(input(">Introduzca el primer número: "))
num2 = int(input(">Introduzca el segundo número: "))
if num1==num2:
    print("Los números son iguales")
elif num1>num2:
    print("el numero %s es mayor que %s" %(num1, num2))
else:
    print("el numero %s es menor que %s" %(num1, num2))
''''''
print("(Ejercicio: 3)")      
numero= int(input("Introduzca un número: "))       
if numero%3==0 and numero%2==0:
     print("El número %s es múltiplo de 2 y múltiplo de 3" %numero)
elif numero%3==0:
    print("El número %s es múltiplo de 3"%numero)
elif numero%2==0:
    print("El número %s es múltiplo de 2"%numero)
''''''
print("(Ejercicio: 4)") 
edad = int(input("Introduzca su edad: "))
if edad>=0 and edad<=12:
    print("Si tienes %s años eres un niño" %edad)
elif edad>=13 and edad<=17:
    print("Si tienes %s años eres un adolescente" %edad)
elif edad>=18 and edad<=29:
    print("Si tienes %s años eres un joven" %edad)
elif edad>29 and edad<=100:
    print("Si tienes %s años eres un adulto" %edad)
''''''
print("(Ejercicio: 5)") 
numero1=int(input("Introduzca el primer número para realizar la media:"))
numero2=int(input("Introduzca el segundo número para realizar la media:"))
numero3=int(input("Introduzca el tercer número para realizar la media:"))
numero4=int(input("Introduzca el cuarto número para realizar la media:"))
media=((numero1+numero2+numero3+numero4)/4)
print(("La media es:"), media)
if numero1>media:
    print(numero1)
if numero2>media:
    print(numero2)
if numero3>media:
    print(numero3)
if numero4>media:
    print(numero4)
''''''
print("Ejercicio: 6)")
caracter= input("Seleccione un carácter de su teclado: ")
if caracter==("A") or caracter==("a"):
    print("La 'A' es la primera vocal")
elif caracter==("E") or caracter==("e"):
    print("La 'E' es la segunda vocal")
elif caracter==("I") or caracter==("i"):
    print("La 'I' es la tercera vocal")
elif caracter==("O") or caracter==("o"):
    print("La 'O' es la cuarta vocal")
elif caracter==("U") or caracter==("u"):
    print("La 'U' es la quinta y última vocal")
else:
    print("El caracter '%s' no es una vocal" %caracter)
''''''
print("Ejercicio: 7)")
estadoCivil=input("Introduzca su estado civil (S-soltero, C-casado, D-divorciado, V-viudo)->")
edad=int(input("Ahora dime tu edad: "))
if estadoCivil==("S") or estadoCivil==("D") and edad<35:
    print("Se le aplicará una retencion del 12%")
elif edad>50:
    print("Se le aplicará una retencion del 8.5%")
elif estadoCivil==("V") or estadoCivil==("C") and edad<35:
    print("Se le aplicará una retencion del 11.3%")
else:
    print("Se le aplicará una retencion del 10.5%")
''''''
print("Ejercicio: 8)")#####TERMINAR#####
hora1=int(input("Hora en formato digital 24h:"))
min1=int(input("Minutos:"))
seg1=int(input("Segundos:"))
hora2=int(input("Seleccione otra hora en formato digital 24h:"))
min2=int(input("Minutos:"))
seg2=int(input("Segundos:"))
print("Hora 1:" ,hora1,min1,seg1) 
print("Hora 2:" ,hora2,min2,seg2)
if hora1>0 and hora1<23 and hora1>hora2:
    print("La hora 1 es mayor")
elif hora1>0 and hora1<23 and hora1=hora2 and min1>0 and min<59 and seg1:
''''''
print("Ejercicio: 9)")
precio=int(input("¿Que precio tiene su producto?"))
producto=input("¿Que producto a elegido? (A,B o C)")
if producto!=("A") and producto!=("B") and producto!=("C"):
    print("ERROR producto incorrecto")
elif producto==("A"):
    print("El precio final es: ",(precio-precio*0.07),"€")
elif producto==("C") or precio<500:
    print("El precio final es: ",(precio-precio*0.12),"€")
else:
    print("El precio final es: ",(precio-precio*0.09),"€")
''''''
print("Ejercicio: 10)")
num1=int(input("Seleccione un número ENTERO:"))
caracter=input("Elija un carácter para la operación:")    
num2=int(input("Seleccione el segundo numero:"))
print(num1,caracter,num2,)
if caracter==("-"):
    print(num1-num2)
elif caracter==("+"):  
    print(num1+num2)
elif caracter==("*"):
    print(num1*num2)
elif caracter==("/"):
    print(num1/num2)
elif caracter==("%"):
    print(num1%num2)
else:
    print("CARÁCTER O NUMERO NO ENCONTRADO")
'''