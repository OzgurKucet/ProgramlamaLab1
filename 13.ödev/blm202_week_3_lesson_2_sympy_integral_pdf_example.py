# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 20:37:35 2020

@author: Ozgur Kucet 170401050

https://github.com/OzgurKucet/ProgramlamaLab1/blob/master/13.%C3%B6dev/blm202_week_3_lesson_2_sympy_integral_pdf_example.py
"""


"""
P(11<x<12)=n(E)/n(S)
 
"""
#E, 11 ile 12 arasında mümkün olan tüm sınıfların kümesidir
#S, olası tüm sınıfların kümesidir—yani, 1 ile 20 arasındaki tüm gerçek sayılar.
#P(x) a probability density function

"""
n(E) sonsuzdur, çünkü olası tüm gerçek sayıları 11 ile 12
arasında saymak imkansızdır; aynı şey n (ler) için de geçerlidir.
Bu nedenle, olasılığı hesaplamak için farklı bir yaklaşıma ihtiyacımız var.
"""

from sympy import pprint

from sympy import Symbol, exp, sqrt, pi, Integral 
x = Symbol('x') 
p = exp(-(x - 10)**2/2)/sqrt(2*pi)
pprint(p)

pprint(Integral(p, (x, 11, 12)).doit().evalf())#11 ile 12 arasında olma olasılığı



