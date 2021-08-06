from methods import makeMatrix,Print
n=5
a=makeMatrix(n)
Print(a)

for i in range(n):
    for j in range(n):
        if j%2==0:
            print(a[i][j],end=' ')
        else:
            print(a[(n-1-i)][j])
    print()
