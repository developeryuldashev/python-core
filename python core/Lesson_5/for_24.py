x,n=2,1
k=1
s=1
for i in range(1,n+1):
    k*=(i)*(2*i-1)
    s+=((-1)**i*x**(2*i))/k
print(s)
