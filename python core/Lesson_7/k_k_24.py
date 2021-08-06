n=6
s=0
s1=0
r=False
while n>0:
    x=float(input('x='))
    r=r or x==0
    if r:
        s+=x
        if x==0:
            s1=s
            s=0
    n-=1
print(s1)