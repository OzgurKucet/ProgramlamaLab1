def Selection_Sort(liste):
    for i in range(len(liste)):
        key = i;
        for j in range(i+1,len(liste)):
            if liste[key] > liste[j]:
                key = j
        liste[i],liste[key] = liste[key],liste[i]


    return liste


dizi = [25,10,5,30,40,2,1,18,7]
Selection_Sort(dizi)
print(dizi)
