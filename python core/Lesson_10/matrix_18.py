a=[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]
s=0
p=1
k=2
for j in range(4):
    if j==k:
        for i in range(len(a)):
            s+=a[i][j]
            p*=a[i][j]
print(s)
print(p)
    