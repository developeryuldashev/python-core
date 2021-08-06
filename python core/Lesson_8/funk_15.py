# a=12345654321
# r=True
# while a>0:
#     l=len(str(a))
#     r=r and a%10==a//(10**l-1)
#     a=a//10
#     l=len(str(a))
#     a=a%(10**(l-1))
# return r


def DigitCount(a):
    t=0
    while a>0:
        a=a//10
        t+=1
    return t

def IsPalendrom(b):
    r=True
    while b>0:
        l=DigitCount(b)
        r=r and b%10==b//(10**(l-1))
        b=b//10
        l=DigitCount(b)
        b=b%(10**(l-1))
    return r
#print(IsPalendrom(121))



n=5
t=0
while n>0:
    x=int(input('x='))
    if IsPalendrom(x):
        t=t+1
    n-=1
print(t)



