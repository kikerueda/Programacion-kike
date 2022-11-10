'''
Created on Nov 10, 2022

@author: estudiante
'''
#Ejercicio 1 
from random import randint

#===============================================================================
# def genera_lista_numeros_aleaotrios(size=100):
#     lista_aleatorios=[]
#     for i in range(size):
#         lista_aleatorios.append(randint(0,1000))
#     return lista_aleatorios
#===============================================================================

lista=[]

for i in range(100):
    lista.append(randint(0, 1000))
print(f"lista de arriba {lista}")

#Ejercicio 1 a)

    
def obtenerElementoMayor(lista):
        
    mayor=lista[0]

    for i in range(len(lista)):
        if lista[i] > mayor:
            mayor=lista[i]
            
    return mayor

#Ejercicio 1 b)




def obtenerElementoMenor(lista):
    menor=lista[0]

    for i in range(len(lista)):
        if lista[i] < menor:
            menor=lista[i]
    return menor


#Ejercicio 1 c)




def sumaNumeros(lista): 
    suma=0
        
    for i in range(100):
    
        suma= suma+lista[i]       
    
    return suma



#Ejercicio 1 d)




def mediaNumeros(lista):

    suma=0    
    for i in range(100):
        suma+=lista[i]   
        
    media=suma/100
    
    return media


#Ejercicio 1 e.)

#===============================================================================
# 
# def sustituirElemento(lista):
#     lista=[]
#     for i in range(100):
#         numero=randint(0,1000)
#         lista.append(numero)
#     return lista
#===============================================================================


#Ejercicio 1 f.)

def mostarElementos(lista):  
    return lista







print("Ejercicio 1 a: ",obtenerElementoMayor(lista))

print("Ejercicio 1 b: ",obtenerElementoMenor(lista))

print("Ejercicio 1 c: ",sumaNumeros(lista))

print("Ejercicio 1 d: ",mediaNumeros(lista)) 

#print("Ejercicio 1 e: ",sustituirElemento(lista))

print("Ejercicio 1 f: ",mostarElementos(lista))