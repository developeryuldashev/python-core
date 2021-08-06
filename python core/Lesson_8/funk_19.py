def Fact2(n):
    p=1
    if n%2==0:
        k=2
    else:
        k=1
    p*=k
    while n!=k:
        k=k+2
        p=p*k
    return p

print(Fact2(4))
print(Fact2(5))
print(Fact2(2))