import os
w=os.listdir('e:/')
files=['1 NTFS', '10-sinf.accdb','dilsho.txt','yusuf.docx']
sanoq=0
for i in files:
    if i in w:
        sanoq+=1
print(sanoq)