a=[3,2,1,4,8,3,5,3,2]
j=0
lens=[]
for i in range(1,len(a)-1):
    if a[i]<a[i-1] and i!=len(a)-1:
        j+=1
    elif j>0:
        if a[i]<a[i-1]:
            lens.append(j+2)
        else:
            lens.append(j+1)
        print(j)
        j=0
print(lens)