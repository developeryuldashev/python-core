k=3
t=0
for i in range(1,k+1):
    print('nabor elementlarini kiriting')
    r=True
    x=int(input('x='))
    while x!=0:
        k=x
        x=int(input('x='))
        r=r and (k<x or x==0)
    if r:
        t+=1
print(t)