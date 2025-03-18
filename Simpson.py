# -*- coding: utf-8 -*-
"""
Created on Mon May 25 12:12:50 2015

@author: alan
"""

import sympy as sp
import numpy

x = sp.symbols("x") # Declaramos los símbolos a usar para las ecuaciones que pediremos

expr_str = input("Introduce tu integral: ") # Pedimos la expresión y la transformamos a formato sympy
expr = sp.sympify(expr_str)
a= input("Introduce tu valor máximo: ")
b= input("Introduce tu valor mínimo: ")
n = input("Introduce n: ")
a = float(a)
b = float(b)
n = float(n)
h = (a-b)/n

A = 0
contador=1
for i in numpy.arange(b+h,a-h,h): #Por todo el número de iteraciones necesarias
    A += (2+2*(contador%2))*expr.subs(x,i)#Si es una iteración n(1) será 4, caso contrario será 2
    contador += 1

A+= expr.subs(x,b) + expr.subs(x,a) #Le agregamos f(a) y f(b)
A = h*A/3
print(A)