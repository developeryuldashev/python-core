#a1x+b1y=c1
#a2x+b2y=c2
a1=1
b1=1
c1=5
a2=2
b2=-1
c2=4

y=((c1/a1)-(c2/a2))/((b1/a1)-(b2/a2))
x=(c1/a1)-(b1/a1)*y
print(f"x={x} va y={y}")