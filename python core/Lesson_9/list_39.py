a=[6,1,3,2,4,3]
t1,t2=0,0
c=0
for i in range(1,len(a)):
    if a[i]>a[i-1] and i!=len(a)-1:
         t1+=1
    elif t1>0:
        c+=1
        t1=0
print(c)
d=0    
for i in range(0,len(a)-1):
    if a[i+1]<a[i]:
         t2+=1
    elif t2>0:
        d+=1
        t2=0
print(d)   