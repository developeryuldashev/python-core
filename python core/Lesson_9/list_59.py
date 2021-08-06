a=[2,4,6,8,10,12]
b=[]
for i in range(len(a)):
    s=0
    for j in range(i+1):
        s+=a[j]
    b.append(s/(i+1))
print(a)
print(b)