n=4
x=int(input('x='))
t=0
while n-1>0:
    k=x
    x=int(input('x='))
    if x>k:
        print(k)
        t+=1
    n-=1
print(t)


