a=[16,8,4,1]
q=a[1]/a[0]
r=True
for i in range(len(a)-1):
    if r and a[i+1]/a[i]==q:
        q=q
    else:
        q=0
print(q)