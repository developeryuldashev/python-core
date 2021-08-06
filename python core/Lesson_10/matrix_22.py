a=[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]
for j in range(1,4,2):
        s=0
        for i in range(len(a)):
            s+=a[i][j]
        print(f"{j+1} ustundagi o'rta arfi :",s/len(a))