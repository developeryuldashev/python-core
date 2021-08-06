a=[1,2,3,4,5,6,3,4,5,8,9]
b=[]
c=[]
n=len(a)
i=n
while i>0:
    b.append(a[i-1])
    c.append(a[i-2])
    i-=2
print(b)
print(c)