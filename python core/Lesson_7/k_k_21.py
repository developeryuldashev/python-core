n=4
x=float(input('x='))
r=True
while n-1>0:
    k=x
    x=float(input('x='))
    r=r and x>k
    n-=1
print(r)