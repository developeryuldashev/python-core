#9-masala
n,s,t=4,0,0
while n>0:
    x=int(input('kiriting x='))
    if x%2==1:
        s+=x
        t+=1
    n-=1
print(s,t)