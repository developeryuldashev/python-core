# a=[]
# m,n=4,4
# d=2
# for i in range(m):
#     a.append(int(input('naborni kiriting :')))
# print(a)

# for i in a:
#     for j in range(n):
#         print(i+j*d,end=' ')
#     print()


#2- usul
from methods import Print
m,n=4,3
xm=[2,3,4]
d=3
a=[]
for i in range(n):
    b=[]
    for j in range(m):
        b.append(xm[i]+d*j)
    a.append(b)
Print(a)
