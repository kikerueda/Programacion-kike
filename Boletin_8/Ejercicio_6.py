'''
Created on Nov 15, 2022

@author: estudiante
'''
elementos=[1,2,3,4,71,87,89]

def estaOrdenada(lista):
    orden=True
    for i in range(1,len(lista)):
        print(lista[i])
        if lista[i]<lista[i-1]:
            orden=False
    return orden
print(estaOrdenada(elementos))