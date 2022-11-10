#===============================================================================
# BOLETIN7#
#===============================================================================
#===============================================================================
#La secuencia siguiente está definida para el conjunto de los números enteros:
#    n → n/2 (n es par)
#    n → 3n + 1 (n es impar)

#Utilizando la función anterior y empezando en 13 se genera la siguiente secuencia
#de números:
#    13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

#Esta secuencia tiene 10 términos y se cree que cualquier secuencia termina en 1.
#Elabora un programa que pida un número n e imprima una cadena con la secuencia
#de números hasta llegar a 1. 
#===============================================================================
print("Ejercicio 5")
numero=int(input("Ingrese un numero: "))

if numero%2==0:
    numero= numero//2
else:
    numero= (numero*3)+1
    
print(numero)
#===============================================================================
# 7. Triángulos. Escribe un programa que pida un número y a continuación pinte un
#triángulo como los siguientes utilizando el número como símbolo.
#===============================================================================
'''
print("Ejercicio 7")
numero=int(input("Insterte un número --> "))
for i in range (numero+1):
    print(f"{numero}"*i)
'''
#===============================================================================
#8.Escribe un programa que pregunte por el tipo de figura que quiere pintar y el tamaño
#del lado de la figura y genere las figuras correspondientes en el siguiente formato
#(los valores 3, 4 y 5 son de ejemplo, podrían pedirse desde 1 hasta 10). 
#===============================================================================
'''
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
'''


    