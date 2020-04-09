# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 16:07:03 2020

@author: Ozgur Kucet
"""

x = 1 
x =  x + x + 1 
print(x) #Çıktısı:3


from sympy import Symbol

x = Symbol('x')
x = x + x + 1
print(x) #Çıktısı:2*x + 1

"""
*******************************************************************************
"""

x = Symbol('x')
y = Symbol('y')

p = x*(x+x)
print(p)# 2*x**2

p = (x+2)*(x+3)
print(p) # (x + 2)*(x + 3)

"""
*******************************************************************************
"""

from sympy import factor,expand
expr = x**2 - y**2 
print(factor(expr))#Çarpanlarına ayrılmış şeklini verir:(x - y)*(x + y)  

factors = factor(expr)#Çarpanlarına ayrılmış şeklini verir
print(expand(factors))#çarpanlara ayrılmış şeklini birleştirir sadeleştirir...


expr = x**3 + 3*x**2*y + 3*x*y**2 + y**3 
factors = factor(expr)#Çarpanlarına ayrılmış şeklini verir
print(expr,"un çarpanlara ayrılmamış şekli:",factors)
 

"""
*******************************************************************************
"""
print("\n\n")

from sympy import pprint # görünüm olarak basmaya yardımcı oluyor...

pprint(factors) #Günlük hayatta kullandığımız sembollere daha yakın basar.

print("\n\n")

"""
Bir kullanıcıdan bir sayı, n girmesini ve bu sayı için bu seriyi yazdırmasını
isteyecek bir program. Seride, x bir semboldür ve n, programın 
kullanıcısı tarafından bir tamsayı girdisidir. Bu serideki n.terim 
tarafından verilir
"""

x = Symbol('x')  
series = x 
n = 5  
for i in range(2, n+1):
    series = series + (x**i)/i
        
pprint(series) #series'i prinlemek:
 




"""
Bu ifadeyi değerlendirmek isterseniz, subs() yöntemini kullanarak semboller 
için sayıları değiştirebilirsiniz
"""

"""
İlk olarak, 91.satır'daki ifadeye başvurmak için yeni bir etiket oluşturuyoruz
ve sonra subs () yöntemini çağırıyoruz. Subs() yönteminin argümanı, 
iki sembol etiketini ve her sembol için yerine koymak istediğimiz sayısal 
değerleri içeren bir Python sözlüğüdür.
"""

expr = x*x + x*y + x*y + y*y
res = expr.subs({x:1, y:2})

print(res) # Bu örneğe göre cevap 9 çıkar...




"""
Subs() yöntemini kullanarak bir sembolü diğerine göre ifade edebilir ve 
buna göre değiştirebilirsiniz. Örneğin, x = 1 − y olarak yazarsak x i
y olarak yazar...
"""

r =  expr.subs({x:1-y}) 
print(r)

print("\n\n")

"""
Seriyi yazdırmaya ek olarak, programımızın belirli bir x değeri için serinin 
değerini bulabilmesini istiyoruz. yani, programımız artık kullanıcıdan
iki girdi alacaktır:
Serideki terimlerin sayısı ve serinin değerinin hesaplanacağı x değeri.
Ardından, program hem seriyi hem de toplamı çıkaracaktır. Aşağıdaki program:
"""

x = Symbol('x')   
series = x
n=5
x_value = 10
for i in range(2, n+1):
    series = series + (x**i)/i
pprint(series)
series_value = series.subs({x:x_value})
print(series_value)





