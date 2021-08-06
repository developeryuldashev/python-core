k=4
x=int(input('x='))
a=x
x=int(input('x='))
b=x
r=True
z=True
while k>2:
    x=int(input('x='))
    r=r and a>b and b<x
    z=r and a<b and b>x
    a=b
    b=x
    k-=1
print( 'x=',(r or z))



