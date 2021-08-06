from methods import makeMatrix,Print
n=5
a=makeMatrix(n)
Print(a)

for i in range(n):
    for j in range(n-i):
        print(a[i][j],end=' ')
    print()
    for k in range(1+i,n):
        print(a[k][n-1-i],end=' ')
    print()
