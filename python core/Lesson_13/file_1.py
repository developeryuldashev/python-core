exept='/\:|=?;[],^<>'
path='file1?.txt'
r=True
for char in path:
    r=r and (char not in exept)
if r:
    f=open(path,'w')
    f.close()
else:
    print('bu nom bilan fayl yaratib bo\'lmaydi')