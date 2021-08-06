a=[5,1,2,4,3,3.6,7]
r=3.5
t=a[0]
b=[]
s=0
for i in range(1,len(a)):
    if abs(t-r)>=abs(a[i]-r):
        s=t
        t=a[i]
        b=[a.index(s),a.index(t)]
print(s,t)
print(b)


