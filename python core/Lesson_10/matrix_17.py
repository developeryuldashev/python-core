#17-masala
a=[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]
s=0
p=1
k=2
# for i in a:
#     if a.index(i)==k:
#         for j in i:
#             s+=j
#             p*=j

for i in range(len(a)):
    if i==k:
        for j in range(4):
            s+=a[i][j]
            p*=a[i][j]
print('s=',s,'\n p=',p)