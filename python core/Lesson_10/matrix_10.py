a=[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]
for i in a:
    for j in range(0,len(i),2):
        print(i[j],end=' ')
    print()
