a=[1,1]
n=6
for i in range(2,n):
    a.append(a[i-1]+a[i-2])
print(a)