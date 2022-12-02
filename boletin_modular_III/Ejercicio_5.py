'''
Created on Nov 28, 2022

@author: estudiante
'''
#==========================================================================================================
# 5. Diseña una función llamada palíndromo que tenga como parámetro de entrada una cadena de caracteres
# y devuelva True si es un palíndromo o False en los demás casos. Una palabra es un palíndromo si
# puede leerse igual de izquierda a derecha o de derecha a izquierda, ignorando los blancos. 
#Por ejemplo: "anilina" o "Dabale arroz a la zorra el abad" Para simplificar el problema, se puede suponer
# que se utilizan caracteres simples, es decir, sin tildes ni diéresis.
#==========================================================================================================


def palindromo(cadena):
    inversa=""
    simple=""
    cadena=cadena.lower()
    for i in range(1,len(cadena)+1):
        if cadena[-i]!=" ":
            inversa+=cadena[-i]
            
    for i in range(len(cadena)):
        if cadena[i]!=" ":
            simple+=cadena[i]        
            
        if simple==inversa:
            igualdad=True
        else:
            igualdad=False
            
    return igualdad

cadena="Dabale arroz a la zorra el abad"
print(palindromo(cadena))
            