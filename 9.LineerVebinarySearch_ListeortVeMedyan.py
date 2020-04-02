# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 22:55:41 2020

@author: Ozgur Kucet
"""

def linearSearchOnlist(liste,item):#en sonuncusunu verir
    found = (-1,-1)
    n = len(liste)
    for indis in range(n):
        if liste[indis] == item:
            found = (liste[indis],indis)
            #break koyarsak ilk bulduğu indisi verir...
    return found
            
liste = [2,3,2,5,8,2,4,3,3,2,8,5,2,4,4,4,4,4]
print(linearSearchOnlist(liste,3))

def ListeOrtalama(liste):
    toplam = 0
    s=0
    for item in liste:
        toplam += item
        s += 1
    return toplam/s

def buble_sort(liste):#Kendim yazdım...

    for i in range(len(liste)):
        for j in range(len(liste)-1):
            if liste[j] > liste[j+1]:
                temp = liste[j]
                liste[j]=liste[j+1]
                liste[j+1] = temp

    return liste

def Binary_search(liste,item):
    found = (-1,-1)
    low = 0
    high = len(liste)-1
    
    while low <= high:
        mid = (low + high)//2
        
        if liste[mid] == item:
            return liste[mid],mid
        elif liste[mid] > item:
            high = mid-1
        else:
            low = mid+1
    return found
    
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


print(ListeOrtalama(liste))

print(buble_sort(liste))

print(Binary_search(liste,5))

liste1 = [1,2,3,4,5,6,7,8,9,10]

print(liste1)
print(MedianBulma(liste1))
