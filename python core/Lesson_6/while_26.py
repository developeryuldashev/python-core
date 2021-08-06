f1=1
f2=1
f3=f1+f2
n=13
while n!=f3:
    f1=f2
    f2=f3
    f3=f1+f2
    if f3==n:
        print(f2,f2+f3)
    else:
        print(0)