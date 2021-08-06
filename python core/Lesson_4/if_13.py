a,b,c=5,6,4
t=0
if a>b and b>c or b>a and c>b:
    t=b
elif b>a and a>c or c>a and a>b:
    t=a
elif a>c and c>b or c>a and b>c:
    t=c
else:
    t='hammasi teng'
print(t)
a,b,c=4,2,6
if a>b:
    x=b
elif a<b:
    x=a
if b>c:
    y=c
elif b<c:
    y=b
if a>c:
    z=c
elif a<c:
    z=a
if z==x:
    m=y
if y==z:
    m=x
if x==y:
    m=z
print(m)