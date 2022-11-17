'''
Created on Nov 14, 2022

@author: estudiante
'''
#===============================================================================
# Realiza una función reverse que reciba una lista y devuelva una nueva lista cuyo
# contenido sea igual a la original pero invertida. Así, dada la lista [‘Di’, ‘buen’, ‘día’, ‘a’,
# ‘papa’], deberá devolver [‘papa’, ‘a’, ‘día’, ‘buen’, ‘Di’].
#===============================================================================
#Ejercicio 5
###Invertir lista
caracteres=[1,2,3,4,5,6,7,8,9]
def revertir(lista):
    invertida = []
    for i in range(1,len(lista)+1):
        invertida.append(lista[-i])
    return invertida
print(revertir(caracteres))