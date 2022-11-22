'''
Created on 22 nov 2022

@author: kiker
'''
#===============================================================================
# 7. Escribir una función denominada encajan que indique si dos fichas de dominó
# encajan o no. Las fichas son recibidas en dos cadenas de texto con el siguiente
# formato: [3,4] [2,5]
#===============================================================================

ficha_1=[2,4]
ficha_2=[3,2]

def validacionEncaje (lista_1, lista_2):
    encajan=False
    if lista_1[0]==lista_2[0] or lista_1[1]==lista_2[1] or lista_1[0]==lista_2[1] or lista_1[1]==lista_2[0]:
        encajan=True
        
    return encajan
print(validacionEncaje(ficha_1, ficha_2))