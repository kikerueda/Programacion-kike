'''
Created on Oct 31, 2022

@author: Kiikerueda
'''
print("#"*45)
print("# Bienvenido al IES Jacarandá!!:            #")
print("    1. Alumnos que han entrado: ")
print("    2. Alumnos que han abandonado el centro: ")
print("    3. Alumnos en el IES: ")
print("    4. Salir ")
print("#"*45)

opcion=int(input("Seleccione una opción (1-4): "))
while opcion<1 or opcion>4:
    opcion=int(input("Seleccione una opción (1-4): "))

ies=0  
while not(opcion==4):  
    
    
    
    if opcion==1:
        entran=int(input("Introduzca la cantidad de alumnos que entran: "))
        ies+=entran
    if opcion==2:
        salen=int(input("Introduzca la cantidad de alumnos que salen: "))
        while salen>ies:
            salen=int(input("Introduzca una cantidad valida de alumnos que salen: "))
        ies-=salen
    if opcion==3:
        print(f"En el centro se encuentran {ies} alumnos:")
    
    opcion=int(input("Seleccione una opción (1-4): "))
    while opcion<1 or opcion>4:
        opcion=int(input("Seleccione una opción (1-4): "))
    

        