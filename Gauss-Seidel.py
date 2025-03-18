# -*- coding: utf-8 -*-
"""
Created on Fri May 29 12:46:05 2015

@author: alan
"""

import numpy as np

num_ecu = int(input("Introduce el número de expresiones: "))
matriz = [[float(input("Coeficiente: ")) for i in range(num_ecu+1)] for i in range(num_ecu)]
valor = [float(0) if (i<num_ecu) else float(1) for i in range(num_ecu+1)] 

error = int(input("Error: "))
print(matriz)
print(valor)

convergen=0
contador=0
while (convergen==0):
    convergen = 1
    for i in range(len(matriz)):
        comp1=round(valor[i],error)
        for j in range(len(matriz[i])):
            if (i!=j): 
                if (j==num_ecu):
                    print("Var_independiente: ",matriz[i][j])
                    valor[i] += matriz[i][j]*valor[j]/matriz[i][i]
                else:
                    valor[i] -= matriz[i][j]*valor[j]/matriz[i][i]
                    
                #result += j*k/matriz[matriz.index(i)][i.index(j)] if (valor[valor.index(k)]==num_ecu)  else (float(-1))*j*k/matriz[matriz.index(i)][i.index(j)]
        print("Valor[",i,"] = ",valor[i])
        comp2=round(valor[i],error)
    if(comp1!=comp2 and contador<50):
        convergen=0
    contador+=1
        # print("Expresión:", i)
       #print("Valor: ", val_n)
       #if(val_n!=round(i,error)):
        #    convergen=0
        