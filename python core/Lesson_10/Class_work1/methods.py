# coding=utf-8
def Print(x):
    for i in x:
        for j in i:
            print(j, end=' ')
        print()

def Input(m,n):
    x = []
    for i in range(m):
        b = []
        for j in range(n):
            b.append(int(input('x[{}][{}]='.format(i,j))))
        print('--------------')
        x.append(b)
    return x

def makeMatrix(m):
    a = []
    for i in range(m):
        b = []
        for j in range(m):
            b.append((i+1)*10+j+1)
        a.append(b)
    return a