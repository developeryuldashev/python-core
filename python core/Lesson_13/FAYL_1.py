excep='/\:|=?";[],^<>'
path="file.txt"
r=True
for i in path:
    r=r and (i not in excep)
if r:
    f=open(path,'w')
    f.close()

