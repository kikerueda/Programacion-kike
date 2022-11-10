'''
Created on Nov 10, 2022

@author: estudiante
'''
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