n=3
r=True
x=float(input('x='))
while n-1>0:
    k=x
    x=float(input('x='))
    r=r and k>x
    n-=1
if r:
    print(0)
else:
    print(1)