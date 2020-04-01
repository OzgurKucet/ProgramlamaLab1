from sympy import FiniteSet
from fractions import Fraction

#FiniteSet sonlu kümelerde kullanılıyor mesela FiniteSet(0,1) dersek bu {0,1} kümesi oluyor...
#from sympy import S, Interval  yaparak Interval(0,1) dersek [0,1] sonsuz kümesini tanımlamış oluruz...
#Fraction kesirli demek Fraction(1,5) = 1/5

s = FiniteSet(1,1,5,Fraction(1,5),1,1,5)

for member in s:
    print(member)

t = FiniteSet(Fraction(1,5),1,5,1,1)

if s == t:
    print("true")


