# n,a,b=5,3,4
# t=[a,b]
# for i in range(2,n):
#     s=0
#     for j in range(i):
#         s+=t[j]
#     t.append(s)
# print(t)

n,a,b=5,3,4
t=[a,b]
for i in range(2,n):
    t.append(sum(t))
print(t)
