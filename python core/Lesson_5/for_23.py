n,x=2,3
s=x
k=1
for i in range(2,n+1):
     k*=(2*i-2)*(2*i-1)
     s+=((-1)**(n+1)*x**(2*i-1))/k
print(s)

