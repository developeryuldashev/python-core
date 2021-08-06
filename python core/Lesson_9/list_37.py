a=[1,2,3,2,1,4,5,3,4,1,2,3]
t1=0
c1=0
t2=0
c2=0
for i in range(1,len(a)):
    if a[i]>a[i-1]:
        t1+=1
    elif t1>0:
        c1+=1
        t1=0
    if a[i]<a[i-1]:
        t2+=1
    elif t2>0:
        c2+=1
        t2=0
print(c1)
print(c2)
