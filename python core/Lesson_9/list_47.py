a=[5,1,2,4,3,7,7,2,1,11]
sanoq=0
for i in range(0,len(a)):
    t=a[i]
    r=True
    for j in range(i+1,len(a)):
        r= r and t!=a[j]
    if r:
        sanoq+=1
    print(sanoq)

print(sanoq)

