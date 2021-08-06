a=[]
m,n=3,4
q=2
for i in range(n):
    a.append(int(input('kirit :')))
print(a)

for i in range(m):
    for j in a:
        print(j*(q**i),end=' ')
    print()