a=[3,1,2,2,2,1]
sanoq=0
for i in range(len(a)):
    t=a[i]
    r=True
    for j in range(i+1,len(a)):
        r=(t==a[j])
    if r:
        sanoq+=1
print(sanoq)