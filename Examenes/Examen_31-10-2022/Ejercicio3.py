'''
Created on Oct 31, 2022

@author: Kiikerueda
'''
size=int(input("¿Cuantos empleados tiene la empresa?: "))
while size<0:
    size=int(input("¿Cuantos empleados tiene la empresa?: "))
    
contador=0
edadesP=0
edadesJ=0
mujeresP=0
hombresP=0
mujeresJ=0
hombresJ=0
python=0
java=0

while contador<size:
    contador+=1
    
    lenguaje=input("Python o Java: ").upper()
    while not (lenguaje=="PYTHON" or lenguaje=="JAVA"):
        lenguaje=input("Python o Java: ").upper()
    if lenguaje=="PYTHON":
        python+=1
        
        edadP=int(input("Introduce tu edad: "))
        while edadP<18 or edadP>65:
            edadP=int(input("Introduce tu edad: "))
        edadesP+=edadP
        
        sexo=input("Sexo (H-M): ").upper()
        while not(sexo=="H" or sexo=="M"):
            sexo=input("Sexo (H-M): ").upper()
        if sexo=="H":
            hombresP+=1
        elif sexo=="M":
            mujeresP+=1           
              
    if lenguaje=="JAVA":
        java+=1
        
        edadJ=int(input("Introduce tu edad: "))
        while edadJ<18 or edadJ>65:
            edadJ=int(input("Introduce tu edad: "))
        edadesJ+=edadJ
        
        sexo=input("Sexo (H-M): ").upper()
        while not(sexo=="H" or sexo=="M"):
            sexo=input("Sexo (H-M): ").upper()
        if sexo=="H":
            hombresJ+=1
        elif sexo=="M":
            mujeresJ+=1
    
    
  

print(f"El {(python/size)*100}% de empleados utiliza Python, de los que {hombresP} son hombres y {mujeresP} mujeres y su edad media {edadesP/(mujeresP+hombresP)}")        
    
print(f"El {(java/size)*100}% de empleados utiliza Java, de los que {hombresJ} son hombres y {mujeresJ} mujeres y su edad media {edadesJ/size}")        
    
        

        

