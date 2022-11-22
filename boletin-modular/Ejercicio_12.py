'''
Created on 22 nov 2022

@author: kiker
'''
#===============================================================================
# 12. Escribe una función unionListas que reciba dos listas y devuelva los elementos que
# pertenecen a una, o bien, a la otra, pero sin repetir ninguno (unión de conjuntos).
#===============================================================================
listadenumeros1=[12,41,32,78,21]
listadenumeros2=[81,78,27,55,41]
def unionListas(lista1, lista2):
    listaUnion=[]
    for i in range(len(lista1)):
        listaUnion.append(lista1[i])
        
    for i in range(len(lista2)):
        if not (lista2[i] in listaUnion):
            listaUnion.append(lista2[i])
    return listaUnion

print(unionListas(listadenumeros1, listadenumeros2))        
            
    