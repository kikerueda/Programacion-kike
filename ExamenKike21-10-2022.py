'''
Created on Oct 21, 2022

@author: Enrique Rueda
'''
#===============================================================================
# En el gimnasio Jacatfitness para el que ya hemos trabajado nos piden que realicemos 
# un programa para determinar si deberías acudir al médico para que te haga una
# revisión, para ello debemos hacer las siguientes preguntas:

     #¿Peso?
     #¿Edad?
     #¿Tipo de vida? (Sedentaria/Activa/Muy activa)

#   El programa terminará si se introduce un peso negativo. 
#   Se deben comprobar que los datos son correctos y si no lo son, 
#   se deben volver a preguntar. Las recomendaciones para ir al médico son:

#    Si tienes más de 70 años y lleva una vida Sedentaria
#    Si pesa más de 100 kg sea cual sea la edad.
#    Si pesa más de 74,4 kg y tiene más de 50 años

#En cualquier otro caso se mostrará “No es urgente que acuda al médico si no 
#tiene problemas de salud”   
#===============================================================================



peso=float(input("¿Cual es tu peso actual?: "))
while peso>300:
        peso=int(input("Introduce un peso válido: "))
while peso>0:
    
    edad=int(input("Introduce tu edad: "))
    while edad<0 or edad>100:
            edad=int(input("Introduce una edad correcta: "))
            
    vida=str(input("¿Que tipo de vida llevas? (Sedentaria/Activa/Muy activa)").upper())
    while not (vida=="SEDENTARIA" or vida=="ACTIVA" or vida=="MUY ACTIVA"):
            vida=str(input("Solo existen estas opciones:(Sedentaria/Activa/Muy activa)").upper())
            
    if peso>0:
        if edad>70 and vida=="SEDENTARIA":
            print("Deberias acudir a una revisión.")
        elif peso>100:
            print("Deberias acudir a una revisión.")
        elif peso>74.4 and edad>50:
            print("Deberias acudir a una revisión.")
        else:
            print("No es urgente que acuda al médico si no tiene problemas de salud")
        
        peso=float(input("¿Cual es tu peso actual?: "))
        while peso>300:
                peso=int(input("Introduce un peso válido: "))

        

    
    