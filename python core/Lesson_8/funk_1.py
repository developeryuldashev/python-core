# def f(x):
#     y=x**x+3*x+2
#     print(y)
# f(2)

# def f(x):
#     y=x**2+3*x+2
#     return y
# a=f(2)
# print(3*a)

# def sign(x):
#     if x<0:
#         return -1
#     elif x>0:
#         return 1
#     else:
#         return 0
# a=sign(-9)
# print(a)

# def Disk(a,b,c):
#     return b**2-4*a*c

# def RootsCount(a,b,c):
#    # D=b**2-4*a*c
#     if Disk(a,b,c)>0:
#         return 2
#     elif Disk(a,b,c)==0:
#         return 1
#     else:
#         return0
#
# l=RootsCount(1,5,6)
# print(l)

# def summa1(a,  b):
#     y=a+b
#     return y
# c=summa1(5,6)
# print(c)

# def salom_ber():
#     print("Assalomu aleykum!")
# print(salom_ber())

# def sign(x):
#     if x<0:
#         print("x soni 0 dan kichikligi uchun: ",-1)
#     elif x==0:
#         print(0)
#     else:
#         print("x soni 0 dan kattaligi uchun: ",1)
# sign(6)
# sign(-5)
#
# def sign(x):
#     if x<0:
#         y=-1
#     elif x==0:
#         y=0
#     else:
#         y=1
#     return  y
# c=sign(6)+5*2
# b=10/sign(-8)
# print(c,'\t',b)

# def ildiz_soni (a, b, c):
#     D=b*b-4*a*c   #bu diskiminantni hisoblash formulasi
#     if D>0:
#         print(" bu tenglama 2 ta ildizga ega")
#     elif D==0:
#         print("bu tenglama 1 ta ildizga ega")
#     else:
#         print("bu tenglama birorta ildizga ega emas")
# ildiz_soni(1,-5,6)
# ildiz_soni(1,-4,4)

n=1
p=1
for i in range(1,n+1):
    p=p*i
print(p)