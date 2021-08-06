a,b,c=6.1,3.2,3
if a<b<c or a>b>c:
    a,b,c=2*a,2*b,2*c
else:
    a,b,c=-a,-b,-c
print(a,b,c)