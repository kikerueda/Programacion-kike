'''
Created on Oct 4, 2022

@author: Enrique Rueda 1DAW-B
'''
print("Bienvenido a Jacafitness".upper())

dia=input("¿Que día tienes disponible para Jacafitness? Indica la primera letra del día en MAYÚSCULA (L;M;X;J;V;S;D;)")

hora=int(input("¿A que hora? (Formato 24h)"))

if dia=="L" and hora>=12 and hora<=13:
    print("Tienes disponible Spinning")

elif dia=="L" and hora>=16 and hora<=19:
    print("Tienes disponible Yoga")

elif dia=="L" and hora>=20 and hora<=21:
    print("Tienes disponible Body combat")

elif dia=="X" and hora>=12 and hora<=13:
    print("Tienes disponible Spinning")

elif dia=="X" and hora>=16 and hora<=19:
    print("Tienes disponible Yoga")

elif dia=="X" and hora>=20 and hora<=21:
    print("Tienes disponible Body combat")

elif dia=="V" and hora>=12 and hora<=13:
    print("Tienes disponible Spinning")

elif dia=="V" and hora>=16 and hora<=19:
    print("Tienes disponible Yoga")

elif dia=="V" and hora>=20 and hora<=21:
    print("Tienes disponible Body combat")

elif dia=="M" and hora>=12 and hora<=13:
    print("Tienes disponible Yoga")

elif dia=="M" and hora>=16 and hora<=19:
    print("Tienes disponible Spinning")

elif dia=="M" and hora>=20 and hora<=21:
    print("Tienes disponible Body combat")

elif dia=="J" and hora>=12 and hora<=13:
    print("Tienes disponible Yoga")

elif dia=="J" and hora>=16 and hora<=19:
    print("Tienes disponible Spinning")

elif dia=="J" and hora>=20 and hora<=21:
    print("Tienes disponible Body combat")
elif dia=="S" or dia=="D":
    print("Recuerda que abrimos de Lunes a Viernes")

else:
    print("No está disponible ninguna clase")

    
