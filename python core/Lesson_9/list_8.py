# a=[2,3,4,5,6]
# t=0
# b=[]
# for i in range(len(a)):
#     if a[i]%2==0:
#         t+=1
#         b.append(a[i])
# print(f"massivda {t} ta juft son bor")
# b.reverse()
# print(b)

# a=[3,7,5,1,9]
# print(a,'\n')
# r=False
# while not True:
#     for i in range(1,len(a)):
#         if a[i]<a[i-1]:
#             a[i],a[i-1]=a[i-1],a[i]
#         print(a)
#     r=True
#     for i in range(1,len(a)):
#         r=r and a[i]>=a[i-1]
#         print(r)


def Sort(a,kamay=False):
    print(a,'\n')
    r=False
    while not r:
        for i in range(1,len(a)):
            if a[i]<a[i-1]:
                a[i],a[i-1]=a[i-1],a[i]
        r=True
        for i in range(1,len(a)):
            r=r and a[i]>=a[i-1]
    if kamay:
        return rew(a)
    else:
        return a



def rew(a):
    b=[]
    for i in range(len(a)-1,-1,-1):
        b.append(a[i])
    return b

a=[3,7,5,1,9,2,60,2]
x=Sort(a,True)
print(x)
