'''
Created on 22 nov 2022

@author: kiker
'''
#===============================================================================
# 13. Escribe una función que, dada una lista de nombres y una letra, devuelva una lista
# con todos los nombres que empiezan por dicha letra. Debe validar los datos.
#===============================================================================
listadenombres=["Lucía","Enrique","Pablo","Alicia","Luis", "Alejandro"]
letra=input("Filtrar por la primera letra: ").upper()

def filtrarNombres(lista):
    listaFiltrada=[]
    for i in range(len(lista)):
        if lista[i][0]==letra:
            listaFiltrada.append(lista[i])          
    return listaFiltrada
print(filtrarNombres(listadenombres))