n=5
t=0
x=int(input('x='))
print(x)
while  n-1>0:
    k=x
    x=int(input('x='))
    if x<k:
        print(x)
        t+=1
    n-=1
print(t)

