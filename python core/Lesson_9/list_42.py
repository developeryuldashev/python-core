a=[5,1,2,1,3,7]
r=3.5
t=a[0]+a[1]
b=[0,1]
for i in range(1,len(a)-1):
    if abs(r-t)>=abs(r-(a[i]+a[i+1])):
        t=a[i]+a[i+1]
        b.append(i)
        b.append(i+1)
        b.remove(b[0])
        b.remove(b[0])
print(b)
