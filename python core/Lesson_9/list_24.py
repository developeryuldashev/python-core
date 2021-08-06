# a=[3,8,13,18,23,28]
# a=[1,3,5,7,9]
# a=[9,7,5,3,1,-1]
# d=a[1]-a[0]
# r=True
# for i in range(len(a)-1):
#     if r and a[i+1]-a[i]==d:
#         d=a[i+1]-a[i]
#     else:
#         d=0
# print(d)

a=[9,7,5,3,1,-1]
d=a[1]-a[0]
r=True
for i in range(2,len(a)-1):
    r and a[i]-a[i-1]==d:
if r:
    print(d)
else:
    print(0)
    