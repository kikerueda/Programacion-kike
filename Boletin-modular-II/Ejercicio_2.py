'''
Created on 26 nov 2022

@author: kiker
'''
#===============================================================================
# Diseñe un método llamado isLeapYear que reciba un número y devuelva False para
# años comunes y True para los años bisiestos. Puede que sepa que un año se considera
# bisiesto si es divisible por 4, a menos que también sea divisible por 100. Un año no es
# bisiesto si es divisible por 100, a menos que también sea divisible por 400.
#===============================================================================
def isLeapYear(year):
    return year%4==0 and (year%100!=0 or year%400==0)

anyo=int(input("¿Es bisiesto?:"))
print(isLeapYear(anyo))

    
    