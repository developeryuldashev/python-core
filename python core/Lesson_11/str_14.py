satr='assa lomu alekum '
r=False
s2=''
s1=''
t=0
for char in satr :
    r=r or char==' '
    if char==' ':
        t+=1
    if r:
        s2+=char
        if t<2:
            s1+=s2
            s2=''
print(s1)