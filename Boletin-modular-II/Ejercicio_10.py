'''
Created on 26 nov 2022

@author: kiker
'''
#===============================================================================
# 10. Diseñe un método llamado isFriendNumber que reciba dos números positivos y
# devuelva True si los números son amigos, False en caso contrario. Dos números se
# consideran amigos si la suma de sus divisores, excepto el número dado, es igual
# al segundo y viceversa.
#===============================================================================
def isFriendNumber(numero1,numero2):
    if numero1>0 and numero2>0:
        sonamigos= True
        divisores1=0
        divisores2=0
        
        for i in range (1,numero1):
            if numero1%i==0:
                divisores1+=i
                
        for i in range (1,numero2):
            if numero2%i==0:
                divisores2+=i
                
        if not(divisores1==numero2 or divisores2==numero1):
            sonamigos=False
            
    return sonamigos

num1=int(input("NUMERO 1:"))
num2=int(input("NUMERO 2:"))
print(isFriendNumber(num1, num2))
