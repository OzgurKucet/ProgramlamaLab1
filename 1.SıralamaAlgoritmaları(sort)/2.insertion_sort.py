"""
def insertion_sort(arr): #Bu insertion sort
    for i in range(1, len(arr)):

        deger = arr[i]

        j = i-1
        while j >=0 and deger< arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = deger
    return arr
"""


def insertion_sort(liste):

    for i in range(1,len(liste)):
        key = liste[i]
        j=i-1
        while j >= 0 and key < liste[j]:
            liste[j+1] = liste[j]
            j-=1
        liste[j+1] = key
    return liste


liste = [3,0,2,5,-1,9,-20,1,2,-44]
print(insertion_sort(liste))
