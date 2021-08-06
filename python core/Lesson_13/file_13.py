import random
def tanlsh(start1,stop1,nechta):
    f = open('sonlar1.txt', 'w')
    for i in range(nechta):
        number=random.randint(start1,stop1)
        f.write(str(number) + '\t')
    f.close()

d=tanlsh(-100,100,100)
f = open('sonlar1.txt','r')
a = f.read()
b = list(a.split())
f.close()
print(b[10])
with open('musbatsonlar.txt','w') as file1, open('manfiysonlar.txt','w') as file2:
    for i in range(0,len(b),2):
        if int(b[i])>0:
            file1.write(str(b[i]+'\n'))
        else:
            file2.write(str(b[i]+'\t'))


