'''
Created on Nov 14, 2022

@author: estudiante
'''
#===============================================================================
# Realiza una función reverse que reciba una lista y devuelva una nueva lista cuyo
# contenido sea igual a la original pero invertida. Así, dada la lista [‘Di’, ‘buen’, ‘día’, ‘a’,
# ‘papa’], deberá devolver [‘papa’, ‘a’, ‘día’, ‘buen’, ‘Di’].
#===============================================================================
numeros=[1,2,3,4,5,6,7,8,9]
def reversar(lista):
    for i in range(len(lista)):    
        guardar=lista[i] 
        escribir=lista[-i]
        lista[i].append(int(escribir))
    return lista
    
print(reversar(numeros))