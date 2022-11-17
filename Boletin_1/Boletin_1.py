'''
@author: kiikerueda
'''
print("3+15", type("3+15"))
print(3+15, type(3+15))
print(str(3+15), type(str(3+15 )))
##Boletin 1       
print ("-------")
print ("EJ2----------------")
print(27%4 + 15/4, type(27%4 + 15/4))
print(37/4**2-2, type(37/4**2-2))
print(9*2/3*10*3, type(9*2/3*10*3))
print((7*3-4*4)**(2/4*2))
print(7>=27 and not (7<=2))
print(24>5 and 10<=10 or 10==5)
print((10>=15 or 23==13) and not(8==8))

print ("EJ5----------------")

A=True
B=True

print("Para A=", A, " y B=", B)

print((A or B) and not (A))
print(not (A or B) and B)
print(A or not (B))
print(not((A and B) and (B or A)))

print("---------------------")

A=False
B=True

print("Para A=", A, " y B=", B)

print((A or B) and not (A))
print(not (A or B) and B)
print(A or not (B))
print(not((A and B) and (B or A)))

print("---------------------")

A=True
B=False

print("Para A=", A, " y B=", B)

print((A or B) and not (A))
print(not (A or B) and B)
print(A or not (B))
print(not((A and B) and (B or A)))

print("---------------------")

A=False
B=False

print("Para A=", A, " y B=", B)

print((A or B) and not (A))
print(not (A or B) and B)
print(A or not (B))
print(not((A and B) and (B or A)))
''''''
print("EJ3-a)----")
#False
precio=10
print(precio>=60 and precio<=420)
precio=50
print(precio>=60 and precio<=420)

#True
precio= 100
print(precio>=60 and precio<=420)
precio= 400
print(precio>=60 and precio<=420)
print("EJ3-b)----")
numero=45
print(numero%2 == 1)
numero=10
print(numero%2 == 1)
print("EJ3-c)------")
#True
saldo=500
dineroSacar=300
print(dineroSacar<=saldo and saldo>=0 and dineroSacar>0)

#False
saldo=500
dineroSacar=10000
print(dineroSacar<=saldo and saldo>=0 and dineroSacar>0)

#False
saldo=500
dineroSacar=0
print(dineroSacar<=saldo and saldo>=0 and dineroSacar>0)

print("EJ3-d)------")
#True
hora=22
minutos=45
print((hora>=0 and hora<=23) and (minutos>=0 and minutos<=59))
#False
hora=25
minutos=45
print((hora>=0 and hora<=23) and (minutos>=0 and minutos<=59))
print("EJ3-d)------")
#False
estadoCivil="S"
print(not(estadoCivil=="S" or estadoCivil=="C" or estadoCivil=="V" or estadoCivil=="D"))
print(estadoCivil!="S" and estadoCivil!="C" and estadoCivil!="V" and estadoCivil!="D")

#True
estadoCivil="F"
print(not(estadoCivil=="S" or estadoCivil=="C" or estadoCivil=="V" or estadoCivil=="D"))
print(estadoCivil!="S" and estadoCivil!="C" and estadoCivil!="V" and estadoCivil!="D")

print("EJ4-a)------")
#False
cantidad=500
print(not(cantidad>=300 or cantidad<0))
cantidad=-5
print(not(cantidad>=300 or cantidad<0))

#True
cantidad=3
print(not(cantidad>=300 or cantidad<0))

print("EJ4-b)------")
#True
edad=20
print(16<edad<22)

print("EJ4-c)----")
'''
#False
respuesta=input("¿Eres mayor de edad?")
print(not(respuesta=="Si" or respuesta=="No"))
'''
print("EJ4-D)-----")
#False
numero=(int(9))
print(not(numero%7==0 or numero%3==0))
#False
numero=(int(14))
print(not(numero%7==0 or numero%3==0))
#True
numero=(int(8))
print(not(numero%7==0 or numero%3==0))

##Boletin 2
print("E1-a)-------------")##############
#True
sueldo_bruto=1000
sueldo_neto=88
porcentajeNeto=88
print(((sueldo_neto/sueldo_bruto) *100)<=88)
#False
sueldo_bruto=1000
sueldo_neto=900
porcentajeNeto=88
print(((sueldo_neto/sueldo_bruto) *100)<=88)

print("E1-b)-------------")
#True
diaMayo=16
print(0<diaMayo<=31)
#False
diaMayo=40
print(0<diaMayo<=31)
print("E1-c)-------------")
#True
num1=9
num2=12
print(num1%3==0 and num2%3==0)
#False
num1=2
num2=12
print(num1%3==0 and num2%3==0)
print("E1-d)-------------")
#True
nota=1
print(0<=nota<=10)
#False
nota=13
print(0<=nota<=10)
print("E1-e)-------------")
#True
nota1=5
nota2=5
nota3=5
print(((nota1+nota2+nota3)/3)>=5)
#False
nota1=4
nota2=5
nota3=5
print(((nota1+nota2+nota3)/3)>=5)
print("E2-a)-------------")
nota1=8
nota2=5
nota3=5
print(nota1>=5 and nota2>=5 and nota3>=5)
print("E2-b)-------------")
#True
saldo=1001
descubierto=1
print(saldo>=1000 and descubierto<=5)
#False
saldo=1001
descubierto=6
print(saldo>=1000 and descubierto<=5)
#False
saldo=800
descubierto=3
print(saldo>=1000 and descubierto<=5)
print("E2-c)-------------")
#True
asignaturasAprobadas=5
asignaturasCurso=8
print(((asignaturasAprobadas/asignaturasCurso)*100)>30)
#False
asignaturasAprobadas=1
asignaturasCurso=8
print(((asignaturasAprobadas/asignaturasCurso)*100)>30)
print("E2-d)-------------")
#True
mes=1
dia=16
print(1<=mes<=12 and 1<=dia<=31)
#False
mes=13
dia=16
print(1<=mes<=12 and 1<=dia<=31)