s='arf_prog.txt'
n=10
a=2
d=3
with open(s,'w') as progressiya:
    for i in range(11):
        progressiya.write(str(a+i*d)+'\n')
