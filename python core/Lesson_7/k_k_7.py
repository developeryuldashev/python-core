#7-masala
n=3
s=0
while n>0:
    x=float(input('kiritng x='))
    if x-int(x)>=0.5:
        x=int(x)+1
    else:
        x=int(x)
    s+=x
    n-=1
    print(x)
print(s)


