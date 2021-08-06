# s='assalomu_aleykum_salom'
# s1='salom'
# n=s.find(s1)
# s2=s[:n]+s[n+len(s1):]
# print(s2)

# def findi(s,s0,i):
#     n=s.find(s0)
#     i-=1
#     while i>0:
#         n=s.find(s0,n+1)
#         i-=1
#     return n
# s='Assalomu alaykum al al ala sal'
# s0='al'
# print(findi(s,s0,3), ' chi indeksda 3 marta uchraydi')
# s=s.replace(s0,'',3)
# print(s)


def findi(s,s0,i):
    n=s.find(s0)
    i-=1
    while i>0:
        n=s.find(s0,n+1)   # bu s0 satrni qidirishni n+1 indeksdan boshlaydi
        i-=1
    return n
s='Assalomu alaykum al al ala sal'
s0='al'
print(findi(s,s0,4))    # bu s0 satr 4 marta nechanchi index dan boshlanishini topib beradi