a,b,c=5,10,2
t=0
while a>c:
    b1=b
    while b1>=c:
        b1-=c
        t+=1
    a-=c
print(t)