a=[6,1,3,2,4,3]
b=[]
b.append(a[0])
b.append(a[len(a)-1])
for i in range(1,len(a)-1):
    if not(a[i]>a[i-1] and a[i]>a[i+1] or a[i]<a[i-1] and a[i]<a[i+1] ):
        b.append(a[i])
print(b)
print(max(b))









    


