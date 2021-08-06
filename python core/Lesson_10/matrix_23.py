a=[
    [1,2,3,4],
    [9,6,7,8],
    [9,10,11,12]
]
for i in a:
    min1=i[0]
    for j in i:
        if min1>=j:
            min1=j
    print(min1)
