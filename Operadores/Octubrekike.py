'''
Created on Oct 10, 2022

@author: estudiante
'''
'''Diseñe un programa que pregunte cuántos números quiere escribir el usuario. Después de la
usuario ingresa todos los números, el programa debe decir el medio de los números. Si el
el usuario ingresa un número incorrecto, el programa debería solicitarlo nuevamente. los mensajes son
el seguimiento:
"¿Cuántos números desea ingresar?" para pedir la cantidad de números.
“Ingrese un número mayor que 0:” para solicitar un número.
“El número no es válido, debe ser mayor a 0” para informar que el número no es
válido.
“El medio es XX.XX” para mostrar el resultado.
'''
cantidad= int(input("¿Cuántos números desea ingresar?"))
while cantidad <=0 :
    cantidad= int(input("¿Cuántos números desea ingresar?"))

total=0
contador=0

while cantidad > contador:
    num=int(input("Ingrese un número mayor que 0:"))
    while num<=0:
        num= int(input("El número no es válido, debe ser mayor a 0"))
    contador = contador + 1
    total = total + num
    
print(f"La media es {total/cantidad}")