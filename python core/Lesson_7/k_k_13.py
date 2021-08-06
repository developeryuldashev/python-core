a=int(input('a='))
print(a)
s=a
r=True
while a!=0:
    a=int(input('a='))
    r=r or a>0 and a%2==0
    if a>0 and a%2==0:
        s+=a
    elif 