f=open('extrimums.txt','r')
a=f.read()
f.close()

b=list(a.split())
k=open('maxs.txt','w')
lastmax=int(b[1])
for i in range(1,len(b)-1):
    if (int(b[i])>=int(b[i-1])and int(b[i])>=int(b[i+1])):
        k.write((b[i])+'\t')
k.close()
