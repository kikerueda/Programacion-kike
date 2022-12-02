'''
Created on Nov 28, 2022

@author: estudiante
'''
#===============================================================================
# 3. Diseñe una función llamada upperCaseInString que tenga como parámetro una cadena de caracteres
# y el método debe devolver cuántos son mayúsculas.
#===============================================================================

def upperCaseInString(cadena):
    caracter=""
    contador=0
    invalid=["0","1","2","3","4","5","6","7","8","9"]
    
    for i in range(len(cadena)):    
        caracter=cadena[i]      
          
        if cadena[i]==caracter.upper():
            contador+=1        
               
        if caracter==" ":
            contador-=1
            
        if caracter in (invalid):
            contador-=1         
                        
    mensaje=f"Tiene {contador} letras mayúsculas."   
    
    return mensaje


prueba="HOLa   A1F5HD     MUnDO"

print(upperCaseInString(prueba))