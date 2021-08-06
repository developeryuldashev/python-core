n,k=4,5
r=True
while n>0:
    x=int(input('kiritilsin x='))
    r=r and x<k
    n-=1
print(r)