'''
Created on Nov 10, 2022

@author: estudiante
'''
#===============================================================================
# 7. Triángulos. Escribe un programa que pida un número y a continuación pinte un
#triángulo como los siguientes utilizando el número como símbolo.
#===============================================================================

print("Ejercicio 7")
numero=int(input("Insterte un número --> "))
for i in range (numero+1):
    print(f"{numero}"*i)