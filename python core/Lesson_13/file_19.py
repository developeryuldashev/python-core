import random
with open('extrimums.txt','w') as file:
    for i in range(10):
        number=random.randint(1,30)
        file.write(str(number)+'\t')
f=open('extrimums.txt','r')
a=f.read()
f.close()

b=list(a.split())
lastmax=int(b[1])
for i in range(1,len(b)-1):
    if (int(b[i])>=int(b[i-1])and int(b[i])>=int(b[i+1])):
        lastmax=int(b[i])
print(lastmax)