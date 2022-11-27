'''
Created on 26 nov 2022

@author: kiker
'''
#===============================================================================
# 9. Diseñe un método llamado getPrimeDivisors que reciba un número positivo como
# parámetro y devuelva una lista que contenga sus divisores primos.
#Si el parámetro no es válido el método debe devolver None.
#===============================================================================

                             # No he sabido terminarlo 
                             
def getPrimeDivisors(numero):
    divisores=[]      
    if numero>0:
        for i in range(2,numero):
            primo=True
            if numero%i==0:
                primo=False
            if primo==True:
                divisores.append(i)
    else:
        divisores=None    
           
    return divisores

print(getPrimeDivisors(300))                
            
        
    
