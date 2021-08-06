a=[3,2,11,7,6]
t=0
b=[]
for i in range(len(a)):
    if a[i]%2==1:
        b.append(a[i])
        t=t+1
print(f"bu massivda {t} ta toq son bor")
b.sort()
print(b,  "a massivdagi toq sonlar o'sish tartibida joylashtirildi")