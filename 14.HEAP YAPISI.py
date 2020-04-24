# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 18:45:20 2020

@author: Ozgur Kucet 170401050
"""

"""
Özet:
    
build_min_heap(array) ,  min_heapify(array, i) ile bir dizinin heap durumuna dönüşmesi sağlanır.
#array=herhangi bir dizi #i ise göderilen nodu un indexi(parentin indexi)

insertItemToHeap(heap_array,key) ise heap durumundaki bir arraye eleman ekleyip yeniden heap durumuna geçirir.
# heap_array = heap durumunda gelen array. #key ise eklenecek sayı

removeItemFrom(myheap_1) heap bir diziden son elemanı çıkartan fonksyon.

heapsort(array):#Heap bir arrayi alır ve sorted bir şekilde geri döndürür.
array=ise heap şeklinde bir array gelir...
"""

def min_heapify(array, i):#Heap durumuna sokmak için kullanılır heapteki elemanlar parentları ile karşılaştırılır.
    left = 2 * i + 1
    right = 2 * i + 2
    length = len(array) - 1
    smallest = i
    if left <= length and array[i] > array[left]:
        smallest = left
    if right <= length and array[smallest] > array[right]:
        smallest = right
    if smallest != i:
        array[i], array[smallest] = array[smallest], array[i]
        min_heapify(array, smallest)
        
        
def build_min_heap(array):#n/2 den 0 a kadar olan nodeları minheapfy e atar.
    for i in reversed(range(len(array)//2)):
        min_heapify(array, i)   

def insertItemToHeap(heap_array,key):#tek bir elemanı heap durumumdaki arraye heap olacak şekilde ekler.
    heap_array.append(key)
    index = len(heap_array)-1
    if index<=0:
        return    
    parent = (index-1)//2
    while parent>=0 and heap_array[parent] > heap_array[index]:
        heap_array[parent],heap_array[index] = heap_array[index],heap_array[parent]            
        index = parent
        parent = (index-1)//2
    
def removeItemFrom(myheap_1):#heapten son elemanı siler...
    index = len(myheap_1)
    if index<=0:
        print("heap boş...")
        return
    myheap_1.pop()
    

def heapsort(array):#Heap bir arrayi alır ve sorted bir şekilde geri döndürür.
    array = array.copy()
    build_min_heap(array)
    sorted_array = []
    for _ in range(len(array)):
        array[0], array[-1] = array[-1], array[0]
        sorted_array.append(array.pop())
        min_heapify(array, 0)
    return sorted_array

    
my_array_1 = [8,10,3,4,7,15,1,2,16]
build_min_heap(my_array_1)
print(my_array_1 )
insertItemToHeap(my_array_1,9)
insertItemToHeap(my_array_1,1)
insertItemToHeap(my_array_1,4)
insertItemToHeap(my_array_1,2)
insertItemToHeap(my_array_1,10)
insertItemToHeap(my_array_1,3)
insertItemToHeap(my_array_1,5)
insertItemToHeap(my_array_1,100)
insertItemToHeap(my_array_1,-4)
removeItemFrom(my_array_1)
removeItemFrom(my_array_1)
removeItemFrom(my_array_1)
removeItemFrom(my_array_1)
removeItemFrom(my_array_1)
removeItemFrom(my_array_1)
removeItemFrom(my_array_1)

print(my_array_1 )
print(sorted(my_array_1))