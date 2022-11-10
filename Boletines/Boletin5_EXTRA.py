'''
Created on Oct 13, 2022

@author: kike rueda
''''''
###Boletín 5 EXTRA###
from PIL.ImageGrab import grab
print("Ejercicio 1")
nota=int(input("Introduzca su nota (/100): "))
if nota>=0 and nota<=49:
    print("Suspuenso")
elif nota>=50 and nota<=59:
    print("Suficiente")
elif nota>=60 and nota<=69:
    print("Ben")
elif nota>=70 and nota<=89:
    print("Notable")
elif nota>=90 and nota<=100:
    print("Sobresaliente")
else:
    print("Introduzca una nota válida (0/100)")
    
''''''
print("Ejercicio 2")







''''''
print("Ejercicio 3")
print("Elige una fecha (dd/mm/yyyy")
fechaDia=int(input("Introduce el dia: "))
fechaMes=int(input("Introduce mes: "))
year=int(input("Introduce el año:"))

while fechaDia<=0 or fechaDia>31:
    print("Introduce un día válido (1-31): ")
    fechaDia=int(input("Introduce el dia: "))
    
while fechaMes<=0 or fechaMes>12:
    print("Introduce un mes válido (1-12): ")
    fechaMes=int(input("Introduce mes: "))
    
while fechaMes==2 and year%4!=0 and fechaDia>28:
    print("Febrero no tiene mas de 28 dias en el año que has introducido")
    fechaDia=int(input("Introduce el dia: "))
      
if year%4==0:
    if fechaMes==1:
        print(f"Han pasado {fechaDia} dias.")
    elif fechaMes==2:
        print(f"Han pasado {fechaDia+31} dias")
    elif fechaMes==3:
        print(f"Han pasado {fechaDia+31+29} dias")
    elif fechaMes==4:
        print(f"Han pasado {fechaDia+31+29+31} dias")    
    elif fechaMes==5:
        print(f"Han pasado {fechaDia+31+29+31+30} dias")    
    elif fechaMes==6:
        print(f"Han pasado {fechaDia+31+29+31+30+31} dias")    
    elif fechaMes==7:
        print(f"Han pasado {fechaDia+31+29+31+30+31+30} dias") 
    elif fechaMes==8:
        print(f"Han pasado {fechaDia+31+29+31+30+31+30+31} dias")    
    elif fechaMes==9:
        print(f"Han pasado {fechaDia+31+29+31+30+31+30+31+31} dias")
    elif fechaMes==10:
        print(f"Han pasado {fechaDia+31+29+31+30+31+30+31+31+30} dias")
    elif fechaMes==11:
        print(f"Han pasado {fechaDia+31+29+31+30+31+30+31+31+30+31} dias")
    elif fechaMes==12:
        print(f"Han pasado {fechaDia+31+29+31+30+31+30+31+31+30+31+30} dias")
else:
    if fechaMes==1:
        print(f"Han pasado {fechaDia} dias.")
    elif fechaMes==2:
        print(f"Han pasado {fechaDia+31} dias")
    elif fechaMes==3:
        print(f"Han pasado {fechaDia+31+28} dias")
    elif fechaMes==4:
        print(f"Han pasado {fechaDia+31+28+31} dias")    
    elif fechaMes==5:
        print(f"Han pasado {fechaDia+31+28+31+30} dias")    
    elif fechaMes==6:
        print(f"Han pasado {fechaDia+31+28+31+30+31} dias")    
    elif fechaMes==7:
        print(f"Han pasado {fechaDia+31+28+31+30+31+30} dias") 
    elif fechaMes==8:
        print(f"Han pasado {fechaDia+31+28+31+30+31+30+31} dias")    
    elif fechaMes==9:
        print(f"Han pasado {fechaDia+31+28+31+30+31+30+31+31} dias")
    elif fechaMes==10:
        print(f"Han pasado {fechaDia+31+28+31+30+31+30+31+31+30} dias")
    elif fechaMes==11:
        print(f"Han pasado {fechaDia+31+28+31+30+31+30+31+31+30+31} dias")
    elif fechaMes==12:
        print(f"Han pasado {fechaDia+31+28+31+30+31+30+31+31+30+31+30} dias")
'''
print("Ejercicio 4")

print("Grupos sanguineos".upper())

print("A / B / AB / 0")

grupo1=(input("Introduce el grupo sanguineo de la 1º persona: ").upper())
grupo2=(input("Introduce el grupo sanguineo de la 2º persona: ").upper())

if (grupo1=="A" and grupo2=="B") or (grupo1=="B" and grupo2=="A") :
    print("No son compatibles.")
    
elif (grupo1=="A" and grupo2=="AB") or (grupo1=="AB" and grupo2=="A"):
    print("Son compatibles, AB es receptor de A")
    
elif grupo1=="A" and grupo2=="A":
    print("Son compatibles")
    
elif (grupo1=="A" and grupo2=="0") or (grupo1=="0" and grupo2=="A"):
    print("Son compatibles, A es receptor de 0")

elif grupo1=="B" and grupo2=="B":
    print("Son compatibles")
    
elif (grupo1=="B" and grupo2=="AB") or (grupo1=="AB" and grupo2=="B"):
    print("Son compatibles, AB es receptor de B")
    
elif (grupo1=="B" and grupo2=="0") or (grupo1=="0" and grupo2=="B"):
    print("Son compatibles, B es receptor de 0")
    
elif (grupo1=="AB" and grupo2=="0") or (grupo1=="0" and grupo2=="AB"):
    print("Son compatibles, AB es receptor de 0")
    
elif grupo1=="0" and grupo2=="0":
    print("Son compatibles")
    
     
    
    
    
    








           
      
    
       
      
    
       
   
       
   