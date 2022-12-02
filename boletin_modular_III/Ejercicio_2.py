'''
Created on Nov 28, 2022

@author: estudiante
'''
#===============================================================================
# 2. Diseñe una función llamada lowCaseInString que tenga como parámetro una cadena de caracteres,
# el método debe devolver cuántos de esos caracteres son minúsculas.
#===============================================================================
def lowCaseInString(cadena):
    caracter=""
    contador=0
    invalid=["0","1","2","3","4","5","6","7","8","9"]
    
    for i in range(len(cadena)):    
        caracter=cadena[i]      
          
        if cadena[i]==caracter.lower():
            contador+=1        
               
        if caracter==" ":
            contador-=1
            
        if caracter in (invalid):
            contador-=1         
                        
    mensaje=f"Tiene {contador} letras minusculas."   
    
    return mensaje


prueba="HOLa   A1F5HD     MUnDO"

print(lowCaseInString(prueba))