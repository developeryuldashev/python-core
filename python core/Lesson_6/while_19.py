# n=1562
# t=0
# str1=''
# while n>=1:
#     t=n%10
#     n//=10
#     str1+=str(t)
# print(int(str1))

n=123456789
c=0
temp=n
while temp>0:
    temp//=10
    c+=1
print(c)
k=0
while n>0:
    k+=(n%10)*10**(c-1)
    n//=10
    c-=1
print(k)

