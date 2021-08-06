m,n=4,6
c=[]
k=0
while k<m:
    c.append(int(input('Naborni kiriting :')))
    k+=1
for i in c:
    for j in range(n):
        print(i,end=' ')
    print()