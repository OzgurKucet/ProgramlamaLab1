# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 02:56:06 2020

@author: Ozgur Kucet
"""


from sympy import Symbol,pprint
import sympy as sym
import sympy.plotting as syp
import matplotlib.pyplot as plt

def faktoriyel(n):
    if n == 0:
        return 1
    else:
        return n * faktoriyel(n-1)

x = Symbol('x')# x istenilen olasılık adedi
lamda=Symbol('lambda')#lamda sürecin verilen ortalama değeri
"""
Kısaca : Lamda bir süreçte bir olayın kaç kez olduğunun ortalama değeridir .
bu ortalama değere bakılarak diğer olayların olma olasılıkların çıkartıldığı bir grafiktir.
"""
part_1= ((lamda**x)*sym.exp(-lamda))
part_2=sym.factorial(x)

olasilik = part_1/part_2#Olasıllığın hesaplandığı formül.
pprint(olasilik)

syp.plot(olasilik.subs({lamda:5}),(x,0,10),title="Poisson Distribution")
syp.show()