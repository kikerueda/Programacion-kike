'''
Created on 26 nov 2022

@author: kiker
'''
#===============================================================================
# Diseñe un método llamado getDayOfWeek que reciba una lista con tres enteros
# (día, mes y año) y devuelva el día de la semana para esa fecha (lunes
# martes, miércoles, jueves, viernes, sábado, domingo).
#
# Puede utilizar el siguiente algoritmo para obtener un número entre 0 (domingo) y 6
# (sábado) correspondiente al día de la semana para una fecha determinada:
#===============================================================================
# a = (14 - mes) / 12
# y = año - a
# m = mes + 12 * a - 2
# d = (día + y + y/4 - y/100 + y/400 + (31*m)/12) mod 7
#===============================================================================
#===============================================================================

def getDayOfWeek(dia,mes,anyo):
    nomdias=["Domingo","Lunes","Martes","Miércoles","Jueves","Viernes","Sábado"] 
    a = (14 - mes) // 12
    y = anyo - a
    m = mes + 12 * a - 2
    d = int(dia + y + y//4 - y//100 + y//400 + (31*m)//12) % 7
    
    return nomdias[d]

dia=int(input("Introduce el día: "))
mes=int(input("Introduce el mes: "))
year=int(input("Introduce el año: "))
print(getDayOfWeek(dia, mes, year))