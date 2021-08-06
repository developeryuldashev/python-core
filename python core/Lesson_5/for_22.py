x,n=2,2
s=1
p=1
for i in range(1,n+1):
    p*=i
    s+=x**i/p
print(s)