a=[2,4,6,8,10,12]
b=[]
for i in range(len(a)):
    s=0
    for j in range(i,len(a)):
        s+=a[j]
    b.append(s/(len(a)-i))
print(b)