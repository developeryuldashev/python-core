massiv=[7,4,7,3,5,10]
toq_sonlar_indexi=[]
juft_sonlar_indexi=[]
n=len(massiv)
for i in range(n):
    if massiv[i]%2==0:
        juft_sonlar_indexi.append(i+1)
    else:
        toq_sonlar_indexi.append(i+1)
print(juft_sonlar_indexi)
toq_sonlar_indexi.reverse()
print(toq_sonlar_indexi)