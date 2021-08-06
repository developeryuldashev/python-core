# a=[
#     [1,2,3,4],
#     [5,6,7,8],
#     [9,10,11,12],
#     [13,14,15,16]
# ]
# for i in range(len(a)):
#     for j in range(4):
#         if j%2==0:
#             print(a[i][j],end=' ')
#         else:
#             print(a[-(i+1)][j],end=' ')
#     print('------')

a=[]
n=5
for i in range(n):
    b=[]
    for j in range(n): 
        b.append((i+1)*10+j+1)
    a.append(b)
print(a)
for i in a:
    for j in i:
        print(j,end=' ')
    print()
print('--------')
for i in range(n):
    for j in  range(n):
        if j%2==0:
            print(a[i][j], end=' ')
        else:
            print(a[-(i+1)][j],end=' ')
    print()
