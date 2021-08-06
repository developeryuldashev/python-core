a=[1,6,5,3,4,5]
r=False
t='bunday element yo\'q'
for i in range(1,len(a)-1):
    if not r and a[i]<a[i-1] and a[i]<a[i+1]:
        t=i
    r=r or a[i]<a[i-1] and a[i]<a[i+1]
print(t)
