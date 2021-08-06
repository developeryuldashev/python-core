a=[
[1,2,3,4],
[5,6,7,8],
[9,10,11,12]]
k=1
for i in a:
        if a.index(i)==k:
            for j in i:
                print(j,end=' ')
        print()
