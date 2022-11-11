'''
Created on Nov 11, 2022

@author: estudiante
'''
#Pasar una fecha numerica a fecha en formato largo.
#1-1-2022 ==> 1 de Enero de 2022.

dia, mes , year= 29,2,2020
def es_bisiesto(yyyy):
    bisiesto= yyyy%4==0 and (yyyy%100!=0 or yyyy%400==0)
    return (bisiesto)

def transformar_formato_largo(dia, mes, year):
    meses=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]

def es_fecha_valida:
    dias_maximo_de_mes=[31,28,31,30,31,30,31,31,30,31,30,31]
    fecha_valida= 1<=mes<=12 and ((1<=dia <=dias_maximo_de_mes ))
    if ((1<=dia <=dias_maximo_de_mes[mes-1] or (es_bisiesto(year) and 1<=dia<=29 and mes==2))):
    
    
        mensaje=(f"{dia} de {meses[mes-1]} de {year}")
    else:
        mensaje=("La fecha introducida no es válida")
        
    return mensaje
               
dia=int(input("Introduce un dia de fecha"))
mes=int(input("Introduce un mes de fecha"))
year=int(input("Introduce un año de fecha"))
print(transformar_formato_largo(dia, mes, year))

while dia>1:
    print(transformar_formato_largo(dia, mes, year))
    dia=int(input("Introduce un dia de fecha"))
    mes=int(input("Introduce un mes de fecha"))
    year=int(input("Introduce un año de fecha"))

    