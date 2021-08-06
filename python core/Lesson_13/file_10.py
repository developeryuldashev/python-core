f=open('arf_prog.txt','r')
s=f.read()
f.close()
a=list(s.split())
yangi=open('clone1.txt','a')
for i in range(len(a)-1,-1,-1):
    yangi.write(str(a[i]+'\t'))
yangi.close()

readr=open('clone1.txt','r')
print(readr.read())
readr.close()