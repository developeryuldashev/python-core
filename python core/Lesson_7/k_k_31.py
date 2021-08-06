k,n=2,3
t=0
while k>0:
    print('nabor elementlarini kiritng')
    r=False
    for i in range(1,n+1):
        x=int(input('x='))
        r=r or x==2
    if r:
        t+=1
    k-=1
print(t)