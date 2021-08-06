x,n=0.5,2
s=0
for i in range(1,n+1):
    s+=((-1)**(i-1)*x**(2*i-1))/(2*i-1)
print(s)