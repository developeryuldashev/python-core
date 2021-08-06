# coding=utf-8
from methods import makeMatrix,Print
m = 5
a = makeMatrix(m)
Print(a)
print('---------------')

for j in range(m):
    for i in range(m-j):
        print(a[i][j],end=' ')
    print()
    for k in range(j+1,m):
        print(a[m-1-j][k], end=' ')
    print()