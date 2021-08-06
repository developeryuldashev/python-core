s='assalomu_aleykum_salom bergan yaxshi salom odam'
s1='salom' 
s2=''
for i in range(len(s)-1,-1,-1):
    s2+=s[i]
print(s2)
s3=''
for j in range(len(s1)-1,-1,-1):
    s3+=s1[j]
print(s3)
s4='inshaalloh'
s5=''
for l in range(len(s4)-1,-1,-1):
    s5+=s[l]
s6=s2.replace(s3,s5)
s7=''
for k in range(len(s6)-1,-1,-1):
    s7+=s6[k]
print(s7)