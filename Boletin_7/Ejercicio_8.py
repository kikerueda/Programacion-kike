'''
Created on Nov 10, 2022

@author: estudiante
'''
#===============================================================================
#8.Escribe un programa que pregunte por el tipo de figura que quiere pintar y el tamaño
#del lado de la figura y genere las figuras correspondientes en el siguiente formato
#(los valores 3, 4 y 5 son de ejemplo, podrían pedirse desde 1 hasta 10). 
#===============================================================================

print("Ejercicio 8")
tipo=str(input("Cuadrados/Triangulos/Rombos; Elige una Figura:").upper())

while not(tipo=="CUADRADOS" or tipo=="TRIANGULOS" or tipo=="ROMBOS"):
    tipo=str(input("Elige una figura disponible:").upper())
    
size=int(input("Seleccione el tamaño (1-10)"))
while size<1 or size>10:
    size=int(input("Seleccione el tamaño (1-10):"))

if tipo=="CUADRADOS":
    for i in range(1, size+1):
        print("*"*size)