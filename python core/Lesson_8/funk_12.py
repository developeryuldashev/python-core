# def IsPrime(n):
#     t=0
#     i=1
#     n1=n
#     r=False
#     while n>0:
        
#         r=(n1%i==0)
#         if r:
#             t+=1
#         i+=1
#         n-=1
#     if t==2:
#         return True
#     else:
#         return False
# y=IsPrime(46)
# print(y)
# p=IsPrime(41)
# q=IsPrime(56)
# w=IsPrime(101)
# print(p,q,w)

# k=10
# j=0
# while k>0:
#     x=int(input('x='))
#     if IsPrime(x):
#         j+=1
#         print(x)
#     k-=1
# print(j)

# for i in range(10):
#     if IsPrime(i):
#         print(i)

def IsPrime(a):
    i=2
    r=False
    while i<=a**(1/2):
        r=r or a%i==0
        i=i+1
    return (not r)
print(IsPrime(53))
    

            


