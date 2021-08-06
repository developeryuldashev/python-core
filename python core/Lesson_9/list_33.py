a=[1,6,5,3,4,5]
t='bunday element yo\'q'
for i in range(1,len(a)-1):
    if a[i]>a[i-1] and a[i]>a[i+1]:
        t=i
print(t)