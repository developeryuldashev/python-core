a=[6,1,3,2,4,3]
t=0
for i in range(len(a)-1):
    if  a[i]>a[i+1]:
        t+=1
print(t)