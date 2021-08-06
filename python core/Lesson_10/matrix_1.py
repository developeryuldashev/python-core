a=[]
m,n=3,4
for i in range(m):
    b=[]
    for j in range(n):
        b.append(10*(i+1))
    a.append(b)
print(a)

# for i in a:
#     for j in i:
#         print(j,end=' ')
#     print()

def Print(a):
    for i in a:
        for j in i:
            print(j,end=' ')
        print()

Print(a)