satr='assa lomu alekum '
r=False
s2=''
s1=''
for char in satr :
    r=r or char==' '
    if r:
        s2+=char
        if char==' ':
            s1+=s2
            s2=''
print(s1)