a=[1,2,3,4,5,6,7,10,11,8,9]
r=True
for i in range(1,len(a)):
    r=r and (a[i]-a[i-1])%2==1
    if not r:
        print(i)
        break
if r:
    print(0)


