'''
Created on Nov 10, 2022

@author: estudiante
'''
#La secuencia siguiente está definida para el conjunto de los números enteros:
#    n → n/2 (n es par)
#    n → 3n + 1 (n es impar)

#Utilizando la función anterior y empezando en 13 se genera la siguiente secuencia
#de números:
#    13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

#Esta secuencia tiene 10 términos y se cree que cualquier secuencia termina en 1.
#Elabora un programa que pida un número n e imprima una cadena con la secuencia
#de números hasta llegar a 1. 
#===============================================================================
print("Ejercicio 5")
numero=int(input("Ingrese un numero: "))

if numero%2==0:
    numero= numero//2
else:
    numero= (numero*3)+1
    
print(numero)