a=[8,5,9,6,1,10]
b=[]
for i in range(len(a)):
    if a[i]%2==0:
        b.append(a[i])
print(len(b),'   ',b)