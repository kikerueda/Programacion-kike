'''
Created on 26 nov 2022

@author: kiker
'''
#===============================================================================
# 7. Diseñe un método llamado isPrime que reciba como valor un número entero positivo 
# mayor que 0 como parámetro. El método debe devolver True si el número es primo o False si
# no es primo. Si el parámetro no es válido, el método debe devolver None.
#===============================================================================


def isPrime(numero):
    primo=True
    if numero>0:
        for i in range(2,numero):
            if numero%i==0:
                primo=False
    else:
        primo=None
    return primo

num=int(input("Introduce el numero para saber si es primo: "))
print(isPrime(num))
    
            
    