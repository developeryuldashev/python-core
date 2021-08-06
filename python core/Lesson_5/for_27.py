n=2
x=0.5
s=1
m=1
summ=x
for i in range(2,n+1):
    s*=(2*i-3)
    m*=(2*i-2)
    summ+=(s*x**(2*i-1))/(m*(2*i-1))
print(round(summ,2))