'''
Created on Sep 27, 2022

@author: Kike Rueda
'''
#·BOLETIN 4·#
'''
print("Ejercicio 1)")
cateto1=int(input("Introduzca la medida del primer cateto: "))
cateto2=int(input("Introduzca la medida del segundo cateto: "))
hipotenusa=(cateto1**2 + cateto2**2)**0.5
if cateto1>0 and cateto2>0:
    print("La hipotenusa es: %s" %hipotenusa)
''''''
print("Ejercicio 2)")
faren=int((input("Temperatura en Farenheit: ")))
print((faren-32)*0.5556,"grados Celsius")
''''''
print("Ejercicio 3)")
num1=int(input("Primer numero:"))
num2=int(input("Segundo numero:"))
num3=int(input("Tercer numero:"))
print("La media es:" , (num1+num2+num3)/3)
''''''
print("Ejercicio 4)")
precio=int(input("Introduzca el precio de su producto: "))
if precio>0:
    print("El precio final es",precio-precio*0.15,"€")
''''''
print("Ejercicio 5)")
num1=int(input("Elige el primer numero: "))
num2=int(input("Segundo numero: "))

if num1>num2:
    print("La distancia es",abs(num1-num2))
elif num2>num1:
    print("La distancia es",abs(num2-num1))
elif num1==num2:
    print("La distancia es 0")
'''   ''' 
print("Ejercicio 6)")
x1=int(input("Elija el primer numero de la primera pareja:"))
x2=int(input("Elija el segundo numero de la primera pareja:"))
y1=int(input("Elija el primer numero de la segunda pareja:"))
y2=int(input("Elija el segundo numero de la segunda pareja:"))
''''''
print("Ejercicio 7)")
num=int(input("Elige un numero: "))
print("Raiz cuadrada: %s" %num**0.5)
print("Raiz cubica: %s" %num**0.3333)
''''''
print("Ejercicio 8)")
m2euro=int(input("Monedas de 2€: "))
m1euro=int(input("Monedas de 1€: "))
m50cnt=int(input("Monedas de 50cent/€: "))
m20cnt=int(input("Monedas de 20cent/€: "))
m10cnt=int(input("Monedas de 10cent/€: "))
cents=(m50cnt*0.50+m20cnt*0.20+m10cnt*0.10)
euros=m2euro*2+m1euro
print((euros+cents),"€")
'''  '''
print("Ejercicio 9)")    

base=int(input("Base: "))
exp=int(input("Exponente: "))
result= (base**exp)
resultN=(base**abs(exp))
if exp>0:
    print("resultado: ", result)
elif exp<0:
    print("resultado: ", 1/resultN)
''''''    
print("Ejercicio 10)")
A=input("Lado (A) en cm: ")
B=input("Lado (B) en cm: ")
C=input("Lado (C) en cm: ")

if A==B and A==C and B==C:
    print("Triangulo equilatero")
elif (int(A)**2)==(int(B)**2 + int(C)**2) or (int(B)**2)==(int(A)**2 + int(C)**2) or (int(C)**2)==(int(B)**2 + int(A)**2) :
    print("Triangulo rectangulo")
elif A==B or A==C or B==C:
    print("Triangulo isosceles")
else:
    print("Triangulo escaleno")
''''''
print("Ejercicio 11)")
year= int(input("Introduce un año: "))    
if year%100==0 :
    print("Año no bisiesto")
elif year%100!=0 and year%400==0 :
    print("Año bisiesto")
elif year%4==0:
    print("Año bisiesto")
else:
    print("Año no bisiesto")
''''''
print ("Ejercicio 12)")###no se hacerlo###

print("Ejercicio 13)")
alumnos= int(input("Nº de alumnos: "))
if alumnos>=100:  
    print("Pago a la compañia: ", 65*alumnos ,"€") 
    print("Cobro por alumno: 65 €")
    
elif alumnos>=50 and alumnos<=99:
    print("Pago a la compañia: ", 70*alumnos ,"€") 
    print("Cobro por alumno: 70 €")

elif alumnos>=30 and alumnos<=49:
    print("Pago a la compañia: ", 95*alumnos ,"€") 
    print("Cobro por alumno: 95 €")
elif alumnos<30:
    print("Pago a la compañia: 4000€") 
    print("Cobro por alumno:",4000/alumnos, "€")
'''    
print("Ejercicio 14)")###no se hacerlo###






'''

print("Ejercicio 15)")
dia=int(input("Seleccione un numero (1-7) respecto a un día de la semana: "))
if dia<=0:
    print("Introduzca un numero valido (1-7)")
elif dia==1:
    print("Lunes")
elif dia==2:
    print("Martes")
elif dia==3:
    print("Miercoles")
elif dia==4:
    print("Jueves") 
elif dia==5:
    print("Viernes")
elif dia==6:
    print("Sabado")
elif dia==7:
    print("Domingo")
else:
    print("Introduzca un numero valido (1-7)")
'''
print("Ejercicio 16)")
mes=int(input("Nº del 1-12 para ver cuantos dias tiene el mes correspondiente: "))
if mes<=0:
    print("Introduzca un numero valido (1-12)")
elif mes<=1:
    print("Enero tiene 31 días")
         
elif mes<=2:
    print("Febrero tiene 28 días")
         
elif mes<=3:
    print("Marzo tiene 31 días")
         
elif mes<=4:
    print("Abril tiene 30 días")  
       
elif mes<=5:
    print("Mayo tiene 31 días")
         
elif mes<=6:
    print("Junio tiene 30 días")
        
elif mes<=7:
    print("Julio tiene 31 días")
        
elif mes<=8:
    print("Agosto tiene 31 días")
        
elif mes<=9:
    print("Septiembre tiene 30 días")
         
elif mes<=10:
    print("Octubre tiene 31 días")
        
elif mes<=11:
    print("Noviembre tiene 30 días")
       
elif mes<=12:
    print("Diciembre tiene 31 días")  
else:
    print("Introduzca un numero valido (1-12)")
    
    

         
              

    



    
    
    
    
    
    
    

