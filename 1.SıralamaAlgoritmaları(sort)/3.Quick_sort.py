
def parcala(dizi,solIndis,sagIndis):
    i = solIndis-1
    pivot = dizi[sagIndis]
    for j in range(solIndis,sagIndis):
        if dizi[j] <= pivot:
            i=i+1
            dizi[i],dizi[j] = dizi[j],dizi[i]
    dizi[i+1],dizi[sagIndis] = dizi[sagIndis],dizi[i+1]
    return i+1


def quick_sort(dizi,solIndis,sagIndis):
   if solIndis<sagIndis:
       pivot = parcala(dizi,solIndis,sagIndis)
       quick_sort(dizi,solIndis,pivot-1)
       quick_sort(dizi,pivot+1,sagIndis)

dizi = [25,10,5,30,40,2,1,18,7]
quick_sort(dizi,0,len(dizi)-1)

print(dizi)
