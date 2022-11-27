'''
Created on 26 nov 2022

@author: kiker
'''
#===============================================================================
# Diseñe un método llamado computeDaysInMonth que devuelva el número de días del
# el mes y el año que se reciben como argumentos. Puede utilizar el método
# leapYear anterior. Si los valores no son válidos el método debe devolver -1.
#===============================================================================

def isLeapYear(year):
    return year%4==0 and (year%100!=0 or year%400==0)

def computeDaysInMonth(mes, anyo):
    
    meses=["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    diasmeses=[31,28,31,30,31,30,31,31,30,31,30,31]
    if (mes<=0 or mes>12) or anyo<0:
        mensaje=-1  
        
    elif mes==2 and isLeapYear(anyo):
        dias=29
        mensaje=(f"El mes de {meses[mes-1]}, tiene {dias} dias en el año {anyo}")
    else:
        dias=diasmeses[mes-1]
        mensaje=(f"El mes de {meses[mes-1]}, tiene {dias} dias en el año {anyo}")
        
    return mensaje
     
year=int(input("Introduce un año (aaaa): "))
mes=int(input("Introduce un mes (mm):"))

print(computeDaysInMonth(mes,year))

    
    