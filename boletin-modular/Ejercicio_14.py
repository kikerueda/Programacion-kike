'''
Created on 22 nov 2022

@author: kiker
'''
#===============================================================================
# 14. Escribe una función que, dada una lista de cadenas, devuelva la cadena más larga.
# Si dos o más cadenas miden lo mismo y son las más largas, la función devolverá la
# que tenga el mayor número de caracteres repetidos .
#===============================================================================

listaCadenas1=["Code","Loro","Coche","Cucurucho", "Casino","Pepino","Carroñero"]

def cadenaMasLarga(lista):
    cadenalarga=lista[0]
    
    for i in range(len(lista)):        
        if len(lista[-i]) > len(cadenalarga):
            cadenalarga=lista[-i]
            
    return cadenalarga

print(cadenaMasLarga(listaCadenas1))
