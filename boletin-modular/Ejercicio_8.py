'''
Created on 22 nov 2022

@author: kiker
'''
#===============================================================================
# 8. Realiza un programa que añada números enteros a una lista hasta que se
# introduzca un número negativo. Haciendo uso de esta lista, elabora funciones que
# devuelvan:
# a. una lista con todos los que sean primos.
# b. el sumatorio
# c. el promedio de los valores.
# d. una lista con el factorial de cada uno de esos números.
#===============================================================================
from _operator import le
numero=0
listadenumeros=[]
while numero>=0:
    numero= int(input(f"Introduzca un numero a la lista {listadenumeros}:"))
    listadenumeros.append(numero)
    
def num_primos(lista):
    numerosprimos=[]
    
    for i in range(len(lista)-1): #-1 porque el ultimo numero es el negativo que cierra el ciclo (no lo cuento)
        
        if (lista[i]==2 or lista[i]%2!=0) and (lista[i]==3 or lista[i]%3!=0) and (lista[i]==5 or lista[i]%5!=0) and (lista[i]==7 or lista[i]%7!=0) and (lista[i]==11 or lista[i]%11!=0):
            numerosprimos.append(lista[i])       
    return numerosprimos

def sumatorio(lista):
    suma=0
    for i in range(len(lista)-1): #-1 porque el ultimo numero es el negativo que cierra el ciclo (no lo cuento)
        suma = suma + lista[i]
    return suma


def valorMedia(lista):
    mediaLista=0
    for i in range(len(lista)-1): #-1 porque el ultimo numero es el negativo que cierra el ciclo (no lo cuento)
        mediaLista+=lista[i]
    mediaLista/=len(lista)
    return mediaLista
    
def calcularfactorial(numero):    
    totalfactorial=1
    for i in range(numero):
        totalfactorial = totalfactorial*(i+1)
    return totalfactorial

def meterFactoriales(lista):
    listafactoriales=[]
    for i in range(len(lista)-1): #-1 porque el ultimo numero es el negativo que cierra el ciclo (no lo cuento)
        listafactoriales.append(calcularfactorial(lista[i]))
    return listafactoriales
        
  
print(num_primos(listadenumeros))
print(sumatorio(listadenumeros))
print(valorMedia(listadenumeros))
print(meterFactoriales(listadenumeros))
