#10-masala
n=4
r=True
while n>0:
    x=int(input('kiritilsin x='))
    r=r and x>0
    n-=1
print(r)