k=3
t=0
for i in range(1,k+1):
    print('nabor elementlarini kiriting')
    r=True
    z=True
    x=int(input('x='))
    while x!=0:
        k=x
        x=int(input('x='))
        r=r and (k<x or x==0)
        z=z and (k>x or x==0)
    if r:
        print(1)
    elif z:
        print(-1)
    else:
        print(0)