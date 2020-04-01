def Shell_sort(liste):
    n = len(liste)
    gap = n//2
    while gap>0:
        for i in range(gap,n):
            temp = liste[i]
            j=i
            while j>=gap and liste[j-gap]>temp:
                liste[j] = liste[j-gap]
                j = j-gap
            liste[j] = temp
        gap//=2
    return liste

liste = [3,0,2,5,-1,9,-20,1,2,-44]
print(Shell_sort(liste))
