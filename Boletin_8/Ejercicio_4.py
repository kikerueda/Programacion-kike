'''
Created on Nov 14, 2022

@author: estudiante
'''
#===============================================================================
# Crea un programa que lea por teclado números de forma sucesiva y los guarde en
# una lista; el proceso de lectura y guardado finalizará cuando metamos un número
# negativo. En ese momento se mostrará el elemento mayor y los números pares.
#===============================================================================
numeros=[]
num=int(input("Intrdocuce numeros en la lista: "))
numeros.append(num)
print(f"lista de numeros --> {numeros}")
while num>=0:
    num=int(input("Intrdocuce numeros en la lista: "))
    numeros.append(num)
    print(f"lista de numeros --> {numeros}")

def obtenerelementomayor(numeros):
    elementomayor=numeros[0]
    for i in range (len(numeros)):
        if numeros[i]>elementomayor:
            elementomayor=numeros[i]
    return elementomayor

def es_par(numeros):
    numerospares=[]
    for i in range(len(numeros)):
        if numeros[i]%2==0:
            numerospares.append(numeros[i])
    return numerospares

print(f"Elemento mayor {obtenerelementomayor(numeros)}")
print(f"Numeros pares --> {es_par(numeros)}")