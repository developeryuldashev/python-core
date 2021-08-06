a,b=15,15
if a>b:
    a,b=a,a
elif b>a:
     a,b=b,b
else:
    a,b=0,0
print(a,b)