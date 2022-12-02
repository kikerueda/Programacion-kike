'''
Created on Nov 28, 2022

@author: estudiante
'''
#===============================================================================
# 1. Diseñe una función llamada characterInString que tenga como parámetros de entrada 
#    una cadena de caracteres y un carácter parámetros de entrada y devuelva 
#    el número de veces que ese carácter aparece en la cadena.
#    Debe determinar si la cadena y el carácter son minúsculas o mayúsculas.
#===============================================================================


def characterInString(cadena,parametro):
    parametro=parametro.upper()
    cadena=cadena.upper()
    contador=0
    for i in range(len(cadena)):
        if parametro==cadena[i]:
            contador+=1
    return contador

string=str(input("Introduce una serie de cadenas: "))
parameter=str(input("Que caracter desea buscar en la cadena: "))
print(characterInString(string, parameter))
