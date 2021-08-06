a=[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]
for i in range(len(a)):
    s=0
    for j in range(4):
        s+=a[i][j]
    mins1=s
    if 