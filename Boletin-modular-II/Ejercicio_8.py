'''
Created on 26 nov 2022

@author: kiker
'''
#===============================================================================
# Diseñe un método llamado solveSecondOrderEquation que reciba tres números enteros
# positivos correspondientes a los coeficientes de una ecuación de segundo orden
#(ax2+bx+c=0) y calcule sus posibles soluciones.
# Si los parámetros no son válidos, el método debe devolver None.
#===============================================================================
                         
#                               ax2+bx+c=0
                        #x=-b±√((b**2)-4*a*c)//2*a
                        
                        
    #===========================================================================
    # x=((-b+((b**2-4*a*c)**1/2))/2*a)
    # x2=((-b-((b**2-4*a*c)**1/2))/2*a)
    #===========================================================================

                


def solveSecondOrderEquation(a,b,c):
    dentroraiz=(b**2)-(4*a*c)
    raiz=dentroraiz**0.5
    x=(-b+raiz)/(2*a)
    x2=(-b-raiz)/(2*a)
    
    if dentroraiz<0:
        mensaje="No tiene solucion real"    

    elif a>=0 and b>=0 and c>=0:
        if x==x2:
            mensaje=f"Solucion doble ={x}"
        else:
            mensaje=f"Las posibles soluciones ={x} , {x2}"
    else:
        mensaje=None
        
    return mensaje

print(solveSecondOrderEquation(2, 18, 5)) 

    
    
    
