a1,a2=1,2
k=3
print(a1)
print(a2)
for i in range(3,k+1):
    ak=(a1+2*a2)/2
    a1=a2
    a2=ak
    print(ak)