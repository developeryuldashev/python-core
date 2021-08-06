a=[7,9,3,1,5,8]
k,l=2,3
s1=0
s=sum(a)
for i in range(k,l+1):
    s1+=a[i]
print(s-s1)