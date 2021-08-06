from math import sin
a,b,n=0,2,2
h=(b-a)/2
x=a
print(h)
for i in range(n+1):
    x+=h
    y=1-sin(x)
    print(round(y,5))

