a=[6,5,7]
# a.reverse()
# print(a)
n=len(a)
# while n>0:
#     print(a[n-1],end='\t')
#     n-=1

for i in range(n):
    print(a[n-1-i],end='\t')

