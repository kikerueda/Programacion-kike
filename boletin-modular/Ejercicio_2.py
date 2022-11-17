'''
Created on Nov 10, 2022

@author: estudiante
'''
lista_numeros=[1,2,3,4,5,6,7,8,9,10]
'''

for i in range(10):
    
    numeros=int(input(f"Añade 10 numeros a la lista ({i}/10): "))
    lista_numeros.append(numeros)
'''    
print(lista_numeros)
#cambio de posicion
for i in range(len(lista_numeros)):

    escribir=lista_numeros[i]
    guardar=lista_numeros[(i+1)%len(lista_numeros)]





print(lista_numeros[-5])

print(escribir, guardar)
