a=[
    [10,2,9,4],
    [5,6,7,8],
    [9,10,11,12]
]
for j in range(4):
    min1=a[0][j]
    for i in range(len(a)):
        if min1>=a[i][j]:
            min1=a[i][j]
    print(min1)
