a=[3,5,9,6,1]
b=[]
for i in range(len(a)):
    if a[i]<5:
        b.append(a[i]*2)
    else:
        b.append(a[i]/2)
print(a)
print(b)
