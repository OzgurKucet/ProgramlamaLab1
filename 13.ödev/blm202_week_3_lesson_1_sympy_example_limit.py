# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 20:26:27 2020

@author: Ozgur Kucet 170401050

https://github.com/OzgurKucet/ProgramlamaLab1/blob/master/13.%C3%B6dev/blm202_week_3_lesson_1_sympy_example_limit.py
"""
from sympy import pprint
from sympy import Symbol, Limit 
t = Symbol('t') 
St = 5*t**2 + 2*t + 8

t1 = Symbol('t1')
delta_t = Symbol('delta_t')

St1 = St.subs({t: t1})
St1_delta = St.subs({t: t1 + delta_t})


pprint((St1_delta-St1)/delta_t)
print("Limiti alınca:")
pprint(Limit((St1_delta-St1)/delta_t, delta_t, 0).doit())#fonksyonun limiti bulunur.