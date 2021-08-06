def Input(m,n):
    a=[]
    for i in range(m):
        b=[]
        for j in range(n):
            b.append(int(input('a[{}][{}]='.format(i,j))))
        a.append(b)
        print('------')
    return a

def Print(a):
    for i in a:
        for j in i:
            print(j,end=' ')
        print()
def makeMatrix(m):
    a = []
    for i in range(m):
        b = []
        for j in range(m):
            b.append((i+1)*10+j+1)
        a.append(b)
    return a
