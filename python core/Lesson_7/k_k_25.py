# n=6
# r=False
# s=0
# s1=0
# while n>0:
#     x=int(input('kirit:'))
#     r=r or x==0
#     if r:
#         s+=x
#         if x==0:
#             s1=s
#             s=0
#     n-=1
# print(s1)

n=8
r=False
s=0
s1=0
while n>0:
    x=int(input('kirit:'))
    r=r or x==0
    if r:
        s+=x
        if x==0:
            s1+=s
            s=0
    n-=1
print(s1)