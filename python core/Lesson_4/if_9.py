x,y=1.28,1.09
if x>y:
    a=y
    b=x
elif x<y:
    a=x
    b=y
else:
    a,b=x,y
print(f"a={a}  b={b}")