a=[-2,8,-4,3,7]
b=[]
c=[]
for i in range(len(a)):
    if a[i]>=0:
        b.append(a[i])
    else:
        c.append(a[i])
print(len(b),'\t',b)
print(len(c),'\t',c)