'''
Created on 26 nov 2022

@author: kiker
'''
#===============================================================================
# 5. Diseña un método llamado powerIt que reciba dos enteros y eleve el primer
# número al segundo. Puedes utilizar el producto o la recursión y comprobar los valores. Si
# no se proporciona ningún exponente, el primer número se eleva a 0.
#===============================================================================
def powerIt (numero, exponente=0):
    if exponente=="":
        resultado=numero**0
    else:   
        resultado=numero**(exponente)
    return resultado

num=int(input("Base: "))
exp=(input("Exponente: "))

print(powerIt(num, exp))