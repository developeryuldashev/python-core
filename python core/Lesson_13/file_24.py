a=[1,2,3,4,3,6,7,8,5,4,8,9]
t=0
c=0
for i in range(1,len(a)):
    if a[i]>a[i-1] and i !=len(a)-1:
        t+=1
    elif t>0:
        c+=1
        t=0
print(c)
