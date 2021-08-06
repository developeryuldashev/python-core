a=[6,1,3,2,8,4,2,5,9]
t=a[0]+a[1]
b=[0,1]
for i in range(1,len(a)-1):
    if a[i]+a[i+1]>=t:
        t=a[i]+a[i+1]
        b.append(i)
        b.append(i+1)
        b.remove(b[0])
        b.remove(b[0])
print(t,b)
print(b[-1],b[-2])