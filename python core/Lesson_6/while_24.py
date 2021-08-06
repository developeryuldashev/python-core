f1=1
f2=1
f3=f1+f2
n=8
r=False
while f3<=n:
    r=r or f3==n
   
    f1=f2
    f2=f3
    f3=f1+f2
    
print(r)
