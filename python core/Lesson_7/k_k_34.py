
n,k=2,3
s1=0
while n>0:
    s=0
    r=False
    for i in range(1,k+1):
        x=int(input('x='))
        r=r or x==2
        s=s+x
    if r:
        print(s)
    else:
        print(0)
    n=n-1