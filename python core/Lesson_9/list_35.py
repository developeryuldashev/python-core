a=[6,1,3,2,4,3,5,3,6,1]
b=[]
for i in range(1,len(a)-1):
    if a[i-1]<a[i] and a[i]>a[i+1]:
        b.append(a[i])      
print(min(b))