# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 17:49:41 2020

@author: Ozgur Kucet
"""


import random

s = random.randint(1,100)

print(s)

def get_n_random_numbers(n=10,min_=-5,max_=5):
    numbers = []
    for i in range(n):
        numbers.append(random.randint(min_,max_))
    return numbers

def my_frequency_with_dict(list):
    frequency_dict = {}
    for item in list:
        if item in frequency_dict:
            frequency_dict[item] = frequency_dict[item]+1
        else:
            frequency_dict[item] = 1
    return frequency_dict

def my_frequency_with_list(list):
    frequency_list = []
    for i in range(len(list)):
        s = False
        for j in range(len(frequency_list)):
            if(list[i]==frequency_list[j][0]):
                frequency_list[j][1] = frequency_list[j][1]+1
                s=True
        if(s==False):
            frequency_list.append([list[i],1])
    return frequency_list

def my_mode_with_dict(my_dict):#mod u buldurur yani en çok geçen sayi listede
    frequency_max = -1
    mode = -1
    for key in my_dict.keys():
        if my_dict[key] > frequency_max:
            frequency_max = my_dict[key]
            mode = key
    return mode,frequency_max
    
def my_mode_with_list(my_list):#mod u buldurur ama sözlükten değil listeden bulur.
    frequency_max = -1
    mode = -1
    for item,frequency in my_list:
        #print(item,frequency)
        if frequency>frequency_max:
            frequency_max = frequency
            mode = item
    return mode,frequency_max
    
    
a = get_n_random_numbers(5,-5,5)
print(a)
print(my_frequency_with_dict(a))
print(my_frequency_with_list(a))
print(my_mode_with_dict(my_frequency_with_dict(a)))
print(my_mode_with_list(my_frequency_with_list(a)))
