'''
Created on Nov 18, 2022

@author: estudiante
'''
#===============================================================================
# 9. Desarrolla un programa que a partir de una lista de números y un entero k, realice la
# llamada a tres funciones: a) para devolver una lista de números con los menores de
# k, b) otra con los mayores y c) otra con aquellos que son múltiplos de k.
#===============================================================================
listadenumeros=[14,5,31,17,78]
k=26
def menoresQuek(lista):
    menores=[]
    for i in range(len(lista)):
        if lista[i]<k:
            menores.append(lista[i])
    return menores

def mayoresQuek(lista):
    mayores=[]
    for i in range(len(lista)):
        if lista[i]>k:
            mayores.append(lista[i])
    return mayores

def multiplosDek(lista):
    multiplos=[]
    for i in range(len(lista)):
        if lista[i]%k==0:
                multiplos.append(lista[i])
    return multiplos
    
    
    
    
print("a)", menoresQuek(listadenumeros))
print("b)", mayoresQuek(listadenumeros))
print("c)", multiplosDek(listadenumeros))            
            