a=[0,2,4,6,8]
b=[1,3,5,7,9]
c=[]
for i in range(len(a)):
    if a[i]>b[i]:
        c.append(b[i])
        c.append(a[i])
    else:
        c.append(a[i])
        c.append(b[i])
print(c)
