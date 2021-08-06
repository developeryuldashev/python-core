a=[]
m,n=3,4
for i in range(n):
    a.append(int(input('naborni kiriting :')))
print(a)

for i in range(m):
    for j in a:
        print(j,end=' ')
    print()