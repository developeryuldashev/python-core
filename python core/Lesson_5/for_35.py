# a1,a2,a3=1,2,3
# n=5
# print(a1,a2,a3,sep='\n')
# for i in range(4,n+1):
#     ak=a3+a2-2*a1
#     a1=a2
#     a2=a3
#     a3=ak
#     print(ak)

a1,a2,a3=1,2,3
n=5
print(a1,a2,a3,end=' ')
for i in range(4,n+1):
    ak=a3+a2-2*a1
    a1=a2
    a2=a3
    a3=ak
    print(ak,end=' ')