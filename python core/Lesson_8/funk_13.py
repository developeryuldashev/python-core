def DigitCount(n):
    t=0
    n1=n
    while n>0:
        n=n//10
        t+=1
    return t
print(DigitCount(321))
print(DigitCount(2))
y=DigitCount(1)
print(y)

