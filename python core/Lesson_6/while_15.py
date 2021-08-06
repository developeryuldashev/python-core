a=1000
p=7
n=0
while a*(1+p/100)**n<1100:
    n+=1
print(n,a*(1+p/100)**n)