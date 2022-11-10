'''
Created on Nov 10, 2022

@author: estudiante
'''
print("Ejercicio 1")
nota=int(input("Introduzca su nota (/100): "))
if nota>=0 and nota<=49:
    print("Suspuenso")
elif nota>=50 and nota<=59:
    print("Suficiente")
elif nota>=60 and nota<=69:
    print("Ben")
elif nota>=70 and nota<=89:
    print("Notable")
elif nota>=90 and nota<=100:
    print("Sobresaliente")
else:
    print("Introduzca una nota válida (0/100)")