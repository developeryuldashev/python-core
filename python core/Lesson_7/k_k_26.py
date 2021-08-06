n,k=5,4
while n>0:
    x=int(input('x='))
    p=1
    for i in range(1,k+1):
        p=p*x
    print(p)
    n-=1

