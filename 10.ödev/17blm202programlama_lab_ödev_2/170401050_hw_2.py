# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 18:04:51 2020

@author: Ozgur Kucet
"""

import csv

def my_frequency_with_dict(list):
    frequency_dict = {}
    for item in list:
        if item in frequency_dict:
            frequency_dict[item] = frequency_dict[item]+1
        else:
            frequency_dict[item] = 1
    return frequency_dict

def my_mode_with_dict(my_dict):#mod u buldurur yani en çok geçen sayi listede
    frequency_max = -1
    mode = -1
    for key in my_dict.keys():
        if my_dict[key] > frequency_max:
            frequency_max = my_dict[key]
            mode = key
    return mode,frequency_max

def ListeOrtalama(liste):
    toplam = 0
    s=0
    for item in liste:
        toplam += int(item)
        s += 1
    return int(toplam/s)

def buble_sort(liste):#Kendim yazdım...

    for i in range(len(liste)):
        for j in range(len(liste)-1):
            if liste[j] > liste[j+1]:
                temp = liste[j]
                liste[j]=liste[j+1]
                liste[j+1] = temp

    return liste

def MedianBulma(liste):#Videoda yanlışlık vardı düzelttim birdaha bak
    #median kısaca sıralanmış listede ortadaki sayıyı bulmak
    liste2 = buble_sort(liste)
    n = len(liste2)
    if n%2 == 1:
        middle = int(n/2)
        median = liste2[middle]
    else:
        middle1 = liste2[int(n/2)-1]
        middle2 = liste2[int(n/2)]
        median = (middle1+middle2)/2
    return median

with open("input_dir_name/input_hw_2.csv","r") as dosya:
    içerik = dosya.read()
    i=0
    insan = içerik.split(";")
    tarih = []
    for i in range(3,len(insan),3):
        tarih.append(insan[i].split("-"))
    
    #print(tarih[0][1])
    cıkısAyı = []
    for i in range(len(tarih)):
        cıkısAyı.append(tarih[i][1])
        
    AyFrekansı = my_frequency_with_dict(cıkısAyı)
    
    for i in range(1,13):
        if i<10:
            a = str(i)
            b = "0"
            c = b+a
            if c in AyFrekansı:
                pass
            else:
                AyFrekansı[c] = 0
        if i>10:
            if str(i) in AyFrekansı:
                pass
            else:
                AyFrekansı[str(i)] = 0
            
print(AyFrekansı)
print()

a = my_mode_with_dict(AyFrekansı)
sayilar = []
for i,j in AyFrekansı.items():
    sayilar.append(j)

sayilar1 = buble_sort(sayilar)

with open("output_dir_name/170401050_hw_2_output.txt","w") as dosya:
    x = MedianBulma(sayilar1)
    dosya.write("Medyan"+" "+str(x)+"\n")
    dosya.write("Ortalama"+" "+str(ListeOrtalama(sayilar1)))