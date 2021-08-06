a=[3,2,1]
b=[5,4,0]
c=[9,8,6]
d=[]
for i in range(len(a)):
    if a[i]>=b[i] and b[i]>=c[i]:
        d.append(a[i])
        d.append(b[i])
        d.append(c[i])
    elif a[i]>b[i] and b[i]<c[i]:
        d.append(a[i])
        d.append(c[i])
        d.append(b[i])
    elif a[i]<b[i] and a[i]>c[i]:
        d.append(b[i])
        d.append(a[i])
        d.append(c[i])
print(c)
