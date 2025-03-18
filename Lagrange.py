# -*- coding: utf-8 -*-
"""
Created on Sun May 24 20:59:53 2015

@author: alan
"""

import sympy as sp

listax_nofloat = []
listay_nofloat = []
xn = input("x: ")#Introducimos el primer valor de x
if xn!= 'nan':
    yn = (input(": "))
contador = 0
while (xn != 'fin' and yn != 'fin'):
    contador +=1
    listax_nofloat.append(xn)
    listay_nofloat.append(yn)
    xn=input("x: ")
    if xn!= 'fin':
        yn=input("y: ")

listax = [float(i) for i in listax_nofloat] #Conversión de la lista de Xs a Float    
listay = [float(i) for i in listay_nofloat] #Conversión de la lista de Ys a Float   
x = sp.symbols("x")
y = 0

for i in range(0,contador):#Sumatoria de elementos
    arriba = 1
    abajo = 1
    for j in range(0,contador):#Producto de ambos elementos, arriba y abajo
        if (i!=j):
            arriba *= (x - listax[j])
            abajo *= (listax[i]-listax[j])
    
    y += (arriba/abajo)*listay[i]#Sumamos los elementos a la misma y
print(sp.expand(y))
print(y.subs(x,input("Introduce el valor a sustituir")))#Valor a evaluar