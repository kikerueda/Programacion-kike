'''
Created on Oct 13, 2022

@author: estudiante
''''''

print("Ejercicio 18")#captura 14/10/2022 13:10
minimo=int(input("Introducza el limite INFERIOR del intervalo: "))
maximo=int(input("Introducza el limite SUPERIOR del intervalo: "))

while minimo>=maximo:
    minimo=int(input("Introducza el limite INFERIOR del intervalo: "))
    maximo=int(input("Introducza el limite SUPERIOR del intervalo: "))
     
numero=int(input(f"Introduce un numero entre {minimo} y {maximo}: "))

suma=0
fuera=0
igual=0

while numero!=0:
    numero=int(input(f"Introduce un numero entre {minimo} y {maximo}: "))
''''''
print("Ejercicio 19")
numero=10
suma=numero
for i in range(2,21):
    numero= numero*2
    suma+=numero
    print(f"{i}º mes {numero}€")
print(f"total {suma}€".upper())
'''
numero=int(input("numero: "))
for i in range (1,numero+1):
    print(f"{numero}"*i)
    
