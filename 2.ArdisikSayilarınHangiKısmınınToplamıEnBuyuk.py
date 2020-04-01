"""
program soyle isliyor:

4 -3 5 -2 -1 2 6 -2 dizisinde ardisik sayilardan(yanyana duran sayılardan hangilerii)
hangileri alınarak toplamlari en büyük olur ?

bu örnekte 4 -3 5 -2 -1 2 6 alınırsa toplamları en büyük dizi bu olur... 11 eder

"""

def Atset():
    liste = [4,-3,5,-2,-1,2,6,-2,-9,9,0]
    max = 0
    for i in range(len(liste)):
        for j in range(i+1,len(liste)):
            #print(i,j)
            t = 0
            for k in range(i,j+1):
                t += liste[k]
            if t > max:
                max = t
                i_1,i_2 = i,j

    return max,i_1,i_2



print(Atset())
