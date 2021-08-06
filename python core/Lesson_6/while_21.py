# n=668
# t=0
# while t%2!=1:
#     t=n%10
#     n=n//10
# print(t)

n=1668
r=False
while n>0:
    r=r or (n%2)==1 
    # print(r)
    n=n//10
print(r)