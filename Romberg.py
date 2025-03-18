# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import sympy as sp
import numpy as np

x = sp.symbols("x") # Declaramos los símbolos a usar para las ecuaciones que pediremos

str_exp =   input("Introduce tu expresión: ") # Pedimos la expresión
expr = sp.sympify(str_exp) # La transformamos al formato de sympy

a = float(input("Introduce a: "))
b = float(input("Introduce b: "))
c = b-a
error = 4
I = [(0) for i in range()
J=(1/2)*(expr.subs(x,a)+expr.subs(x,b))
I.append(c*J)
print(I[0])
i=int(1)
comp1=round(I[0,error)
while (True):
    J += expr.subs(x,a+(2*i-1)/2**i)
    for j in np.arange(i):
        if j:
            I[i].append((1/(4**j-1))*(4**j*I[i][j-1]-I[i-1][j-1]))
        else:
            I.append(c*J/2**i)
            print(I[i][0])
    print(I[i-1][i-1])
    omp1=round(I[(i-1)[i-1]],error)
    comp2=round(I[i][i],error)
    
    #print(comp2)
    #if (comp1==comp2):
    #5    break;
    i+=1