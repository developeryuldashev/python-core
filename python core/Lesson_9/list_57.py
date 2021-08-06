a=[2,4,8,7,3,9]
i=0
b=[]
while i<len(a):
    b.append(a[i])
    i+=2
j=1
while j<len(a):
    b.append(a[j])
    j+=2
print(a)
print(b)
