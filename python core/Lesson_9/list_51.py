a=[3,5,9,6,1]
b=[2,5,7,4,9]
c=[]
for i in range(0,5):
    if a[i]==b[i]:
        c.append(a[i])
        # a.remove(a[i])
        # b.remove(b[i])
    else:
       
        t=a[i]
        a[i]=b[i]
        b[i]=t
print(a,'\n',b)
print(c)
for i in range(len(c)):
    a.remove(c[i])
    b.remove(c[i])
print(a,'\n',b)