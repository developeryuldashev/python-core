a,b,c=9,8,6
if a>b and b>c or b>a and a>c:
    t=a+b
elif  c>b and b>a or b>c and c>a:
    t=c+b
elif  c>a and a>b or a>c and  c>b:
    t=c+a
print(t)