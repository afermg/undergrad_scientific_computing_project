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

for n in np.arange(x0,xf,h)):#Espacio a comparar entre intervalo
    y0 += h * expr.subs([(x,n),(y,y0)])     #yn+1=h*f(x)

print(y0)