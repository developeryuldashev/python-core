import random
# with open('extrimums.txt','w') as file:
#     for i in range(10):
#         number=random.randint(1,30)
#         file.write(str(number)+'\t')
f=open('extrimums.txt','r')
a=f.read()
f.close()

b=list(a.split())
r=False
firstmax=int(b[1])
for i in range(1,len(b)-1):
    if (not r) and (int(b[i])>=int(b[i-1])and int(b[i])>=int(b[i+1])):
        firstmax=int(b[i])
    r =r or (int(b[i]) >= int(b[i - 1]) and int(b[i]) >= int(b[i + 1]))
print(firstmax)


