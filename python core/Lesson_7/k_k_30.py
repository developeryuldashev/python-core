n,k=2,3
s1=0
while n>0:
    s=0
    for i in range(1,k+1):
        x=int(input('x='))
        s=s+x
    s1=s1+s
    print(f" nabordagi sonlar yig'indisi {s}")
    n=n-1
print('barcha naborda gi sonlar yig\'indisi =',s1)