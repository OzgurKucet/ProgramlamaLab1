
#Sözlükler şöyle tanımlanır sozluk = {1:1,2:4,3:9,4:16,-2:4} mesela sözlük[2] dediğimizde bize 4 değerini verir
#sözlük[-2] dersekte 4 geri döner...

def look_up(d,v): #d burada dictionary oluyor v ise kaç tane tekrar ettiği
    for k in d:
        if d[k]==v:
            return k
    return -1

def my_h(list1):
    my_d = dict()
    for i in list1:
        if i in my_d:
            my_d[i] = my_d[i]+1
        else:
            my_d[i] = 1
    return my_d

liste = [0,5,25,100,5,50,100,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]
print(my_h(liste))
print(look_up(my_h(liste),24)) #24 kere tekrar eden 5 var onu döndürür.
print(look_up(my_h(liste),2)) #2 kere tekrar eden 100 var onu döndürür.
print(look_up(my_h(liste),12)) #12 kere tekrar yok -1 döndürür...

