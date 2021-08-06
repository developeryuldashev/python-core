def Fact(n):
    p=1
    i=1
    while n>0:
        p=p*i
        i+=1
        n-=1
    return p
print(Fact(5))

k=6
while k>0:
    x=int(input('x='))
    p=Fact(x)
    k-=1
    print(p)
