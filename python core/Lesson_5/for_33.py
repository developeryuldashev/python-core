f1=1
f2=1
n=4
for i in range(2,n+1):
    f3=f1+f2
    f1=f2
    f2=f3
    print(f3)