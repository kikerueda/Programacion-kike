'''
Created on Nov 28, 2022

@author: estudiante
'''
#===============================================================================
# 4. Diseñe una función llamada numberInString que reciba una cadena de caracteres como
# parámetro y devuelva cuántos de ellos son números.
#===============================================================================
def numberInString(cadena):
    contador=0
    valid=["0","1","2","3","4","5","6","7","8","9"]
    
    for i in range(len(cadena)):         
        if cadena[i]in valid:
            contador+=1
                     
    mensaje=f"Tiene {contador} numeros."   
    
    return mensaje


prueba="HOLa   A1F5HD     MUnDO"

print(numberInString(prueba))