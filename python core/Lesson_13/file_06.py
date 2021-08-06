k=200
f=open('son_yoz.txt','r')
s=f.read()
f.close()
a=list(s.split())
if k<len(a):
    print(a[k])
else:
    print(-1)
