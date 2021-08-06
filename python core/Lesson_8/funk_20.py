# def Fib(k):
#     f1=1
#     f2=1
#     t=2
#     while k!=t:
#         t+=1
#         f3=f1+f2
#         f1=f2
#         f2=f3
        
#     return f2

# print(Fib(4))
# print(Fib(5))
# print(Fib(6))
# print(Fib(7))
# print(Fib(8))

def fib(n):
    f1,f2=1,1
    n-=2
    while n>0:
        fn=f1+f2
        f1,f2=f2,fn
        n-=1
    return f2
for i in range(1,8):
    print(fib(i))
