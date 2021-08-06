a=[6,1,3,2,4,3]
k=3.16
t=abs(a[0]-k)
for i in range(1,len(a)):
    if abs(a[i]-k)<t:
        t=a[i]
print(t)