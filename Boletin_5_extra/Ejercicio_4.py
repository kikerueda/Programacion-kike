'''
Created on Nov 10, 2022

@author: estudiante
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
    