x,n=0.5,2
s=1
k_s=1
k_m=1
for i in range(1,n+1):
    if 2*i-3<=0:
        k_s=1
    k_m*=2*i
    s+=((-1)**(i-1)*k_s*x*(2*i-1))/k_m
print(s,k_s,k_m)     