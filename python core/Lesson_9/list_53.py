a=[3,5,9,6,1]
b=[2,5,7,4,9]
c=[]
for i in range(len(a)):
    if a[i]>=b[i]:
        c.append(a[i])
    else:
        c.append(b[i])
print(a)
print(b)
print(c)