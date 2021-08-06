a=[2,4,8,7,3,9]
b=[]
for i in range(len(a)):
    s=0
    for j in range(i+1):
        s+=a[j]
    b.append(s)
print(a)
print(b)