# 8-masala
n,s,t=4,0,0
while n>0:
    x=int(input('kiritng x='))
    if x%2==0:
        s+=x
        t+=1
        print(x)
    n-=1
print(s,t)
