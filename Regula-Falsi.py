# -*- coding: utf-8 -*-
"""
Created on Fri May  8 14:19:25 2015

@author: alan
"""

import sympy as sp
import numpy
from mpmath import *

expr =   sp.sympify(input("Introduce tu expresión: ")) # Pedimos la expresión y la transformamos a formato sympy

x = sp.symbols("x") # Declaramos los símbolos a usar para las ecuaciones que pediremos
#Parametros para Tabulacion
menor = -2
mayor = 0
diferencia = 1# Establecemos un rango para buscar el cambio de signo
 #Declaramos vector para guardar los pivotes
pivotes = []
centros = []
xn, k = sp.symbols("xn, k")#Declaramos las variables para nuestra funcion
fn = sp.sympify((-k*expr.subs(x,xn)+xn*expr.subs(x,k)) / (-expr.subs(x,xn)+expr.subs(x,k))) #Hacemos la funcion
for n in numpy.arange(menor,mayor,diferencia): #Iteración para buscar cambios de signo y agregarlos a la lista
    if (numpy.sign(expr.subs(x,n))!=(numpy.sign(expr.subs(x,n+diferencia)))):#Si encontramos un cambio de signo
        for nums in numpy.arange(n,n+diferencia,diferencia/5):#Buscamos dentro de ese rango para acercarnos antes de usar NR
               if (numpy.sign(expr.subs(x,nums))!=(numpy.sign(expr.subs(x,nums+diferencia/5)))):#Al reencontrar el cambio de signo
                   if (expr.subs(x,nums)*(expr.subs(x,nums)+expr.subs(x,nums+diferencia/5))/2)<0:# Asignamos el pivote segun f(x)*punto medio <0 
                       pivotes.append(nums)#Agregamos el numero anterior al cambio con el acercamiento
                       centros.append(nums+diferencia/10)#Agregamos el punto medio para que sea x0
                   else:
                        pivotes.append(nums+diferencia/5)#Caso contrario agregamos los del otro lado                       
                        centros.append(nums+diferencia/10)
                        
pivotes_flotantes = [float(i) for i in pivotes]#Convertimos las dos listas a float
centros_flotantes = [float(i) for i in centros]

#Parametros iteraciones
error = 6 #Establecemos el numero de decimales cuyo error buscamos
Max_iter = 50 #Maximas iteraciones

i=0
for n in pivotes_flotantes:# Por cada pivote que hayamos encontrado
    contador = 0 
    xm = fn.subs([(k,n),(xn,centros_flotantes[i])] )
    print(xm)    
    comp1 = round(xm,error) #Sacamos el primer valor a comparar como las sustitucion de estos
    xm = fn.subs([(k,n),(xn,xm)] )#Cambiamos el valor de Xn por el de la ultima sustitucion       
    print(xm)    
    comp2 = round(xm,error)  #Sacamos el segundo valor a comparar como la sustitucion con el nuevo Xn
    i += 1        
    while (comp1!=comp2 and contador< Max_iter) :#Mientras los valores sean diferentes repetimos el procedimiento
        contador += 1     
        comp1 = comp2
        xm = fn.subs([(k,n),(xn,xm)])    
        comp2 = round(xm,error)
        print(comp1,"\t",comp2)