n=5
if n%2==0:
    m=n/2
else:
    m=(n+1)/2
r=True
x=int(input('kirit:'))
n-=1
while n>0:
    c=x
    x=int(input('kirit:'))
    if n>=m:
        r=r and x>c
    else:
        r=r and x<c
    n-=1
print(r) 