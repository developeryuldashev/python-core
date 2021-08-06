#18-masala
a=[6,8,5,5,4,5]
r=False
n=len(a)
i=0
max1='a[n] dan katta son yoq'
while n-1>i:
    if (not r) and a[i]<a[n-1]:
        max1=a[i]
    r=r or a[i]<a[n-1]
    i+=1
print(max1)
