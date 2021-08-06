a=[5,2,1,4 ,10,3,6,7,11,8]
a1=a.copy()
a1.sort()
b=[]
r=False
for i in range(len(a)):
    b.append(i+1)
if a1==b:
    print(0)
else:
    for i in a:
        if not i in b:
            print(a.index(i))




