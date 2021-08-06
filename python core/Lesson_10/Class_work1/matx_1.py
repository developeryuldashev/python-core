  # a=[]
# m,n=3,4
# for i in range(m):
#     b=[]
#     for j in range(n):
#         b.append((i+1)*10)
#     a.append(b)
# for i in a:
#     for j in i:
#         print(j,end=' ')
#     print()

from methods import Print,Input
a=[]
m,n=3,4
for i in range(m):
    b=[]
    for j in range(n):
        b.append((j+1)*10)
    a.append(b)
Print(a)
# for i in a:
#     for j in i:
#         print(j,end=' ')
#     print()