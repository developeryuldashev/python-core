a,b,c=50,20,10
if abs(a-b)>abs(a-c):
    c,t=c,abs(a-c)
    print(c,t)
else:
    b,t=b,abs(a-b)
    print(b,t)

