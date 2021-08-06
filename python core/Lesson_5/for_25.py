x,n=3.0,2
p=1
s=0
for i in range(1,n+1):
    s+=((-1)**(i-1)*x**i)/i
print(s)