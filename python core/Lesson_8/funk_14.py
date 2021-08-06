def DigitN(k,n):
    n1=n
    t=0
    i=0
    d=0
    while n>0:
        n=n//10
        d+=1
    # print(d)
    if d>=k: 
        while n1>0:
            i=n1%10
            n1=n1//10
            t+=1
            if t==k:
                return i
    else:
        return(-1)
f=DigitN(5,1234567890)
print(f)
print(DigitN(1,6))

