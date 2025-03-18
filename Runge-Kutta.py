# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 14:34:38 2015

@author: alan
"""

# -*- coding: utf-8 -*-
"""
Created on Mon May 25 12:51:17 2015

@author: alan
"""

import sympy as sp
import numpy as np

x, y = sp.symbols("x, y") # Declaramos los símbolos a usar para las ecuaciones que pediremos
expr =   sp.sympify(input("Introduce tu expresión: ")) # Pedimos la expresión y la transformamos

x0 = float(input("x0: "))#Pedimos el valor de x inicial
y0 = float(input("y0: "))#Pedimos el valor de y inicial
xf = float(input("xf: "))#Pedimos el valor de x final
h = float(input("h: "))#Pedimos el intervalo de iteraciones

for n in np.arange(x0,xf,h):#Espacio a comparar entre intervalo
    k1=h*expr.subs([(x,n),(y,y0)])
    k2=h*expr.subs([(x,n+h/2),(y,y0+k1/2)])
    k3=h*expr.subs([(x,n+h/2),(y,y0+k2/2)])
    k4=h*expr.subs([(x,n+h),(y,y0+k3)])
    y0 += (1/6)*(k1+2*k2+2*k3+k4)    #yn+1=h*f(x)

print(y0)