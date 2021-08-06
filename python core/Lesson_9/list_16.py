#16-masala
a=[1,3,4,12,5,6,8,9]
n=len(a)
m=n//2
i=0
while m>i:
    print(a[i],a[n-1-i], end=' ')
    i+=1
if n%2==1:
    print(a[m])   

