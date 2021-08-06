a=[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]
for i in a:
    if a.index(i)%2==0:
        for j in i:
            print(j,end=' ')
    print()
    if a.index(i)%2==1:
        for k in range(len(i)-1,-1,-1):
            print(i[k],end=' ')
    print()