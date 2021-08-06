# n=2156
# t=0
# k=False
# while k!=True:
#     t=n%10
#     n//=10
#     k=(t==2)
#     if t/2==1:
#         print(k)
#     else:
#         print(False)

n=134243
r=False
while n>0:
    r=r or (n%10)==2
    n//=10
print(r)
