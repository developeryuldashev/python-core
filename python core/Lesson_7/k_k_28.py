n=5
while n>0:
    p=1
    x=int(input('x='))
    for i in range(1,n+1):
        p=p*x
    print(p)
    n-=1
    