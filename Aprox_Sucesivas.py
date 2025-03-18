# -*- coding: utf-8 -*-
"""
Created on Fri May  8 14:19:25 2015

@author: alan
"""

import sympy as sp
import numpy

x = sp.symbols("x") # Declaramos los símbolos a usar para las ecuaciones que pediremos

str_exp =   input("Introduce tu expresión: ") # Pedimos la expresión
expr = sp.sympify(str_exp) # La transformamos al formato de sympy

str_despeje =   input("Introduce el despeje de x: ") # Volvemos a pedir y a transformar para el despeje
despeje = sp.sympify(str_despeje)

menor = float(input("Menor: "))
mayor = float(input("Mayor: "))
diferencia = float(input("Diferencia"))# Establecemos un rango para buscar el cambio de signo
zeros = [] #Declaramos vector para guardar los ceros
for n in numpy.arange(menor,mayor,diferencia): #Iteración para buscar cambios de signo y agregarlos a la lista
    print(n)
    if (numpy.sign(expr.subs(x,n))!=(numpy.sign(expr.subs(x,n+diferencia)))):
        zeros.append(n+diferencia/2)

ceros_flotantes = [float(i) for i in zeros] #Conversión de la lista de X0s a Float
print(ceros_flotantes)
error = 4 #Establecemos el numero de decimales cuyo error buscamos
Max_iter = 50 #Maximas iteraciones
 #Redondeamos
for n in ceros_flotantes:
    print("\n")
    print(n)
    contador = 0 #Inicializamos contador
    comp1 = n #Valor para comparar la primera iteración X0
    comp2 = round(despeje.subs(x,n),error) #Y para comparar la primera iteración
    num = n # X0
    while (comp1 != comp2 and contador < Max_iter): #Mientras X != f(x) con el error que tenemos
        contador += 1
        num = despeje.subs(x,num) # Xn+1 = f(Xn)
        comp1 = comp2 #Sustituimos los valores que vamos a comparar para seguir iterando
        comp2 = round(despeje.subs(x,num),error)
        print(comp1)
        print(comp2)