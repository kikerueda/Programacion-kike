'''
Created on 26 nov 2022

@author: kiker
'''
#===============================================================================
# Diseñe un método llamado computeFactorial que reciba un número entero positivo y
# devuelva el factorial de ese número. Si el número es negativo el método debe
# retornar Ninguno.
#===============================================================================

def computeFacturial(num):
    factorial=1
    for i in range(num):
        factorial=factorial*(i+1)
    if num>=0:
        mensaje=factorial
    else:
        mensaje= None
        
    return mensaje


numero=int(input("Ingrese un numero para recibir su factorial: "))    
print(computeFacturial(numero))
    
        
























def calcularfactorial(numero):    
    totalfactorial=1
    for i in range(numero):
        totalfactorial = totalfactorial*(i+1)
    return totalfactorial