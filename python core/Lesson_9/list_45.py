a=[5,1,2,12,3,7,11,7.5]
r=abs(a[0]-a[1])
for i in range(len(a)):
    t=a[i]
    for j in range(i+1,len(a)):
        if r>=abs(a[i]-a[j]):
            r=abs(a[i]-a[j])
            b=[i,j]
print(b)
