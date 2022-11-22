'''
Created on 22 nov 2022

@author: kiker
'''
#===============================================================================
# 11. Escribe una función intersect que reciba dos listas y devuelva otra lista con los
# elementos que son comunes a ambas, sin repetir ninguno.
#===============================================================================
from code import interact
listadenumeros_1=[10,42,73,94,25,36,36]
listadenumeros_2=[36,24,37,18,92,36,42]

def interset(lista1, lista2):
    comun=[]
       
    for i in range(len(lista1)):
        if lista1[i] in lista2 and not (lista1[i] in comun):
            comun.append(lista1[i])
    return comun

print(interset(listadenumeros_1, listadenumeros_2))      