import os
w=os.listdir('e:/')
files=['INSTAL', 'Islom Karimov', 'Javob.docx','isjdnf.txt','komil.pdf']
sanoq=0
for i in files:
    if i in w:
        sanoq+=1
print(sanoq)