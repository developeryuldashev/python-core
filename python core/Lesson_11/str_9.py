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
n=s2.find(s3)
s4=s2[:n]+s2[n+len(s3):]
print(s4)
s5=''
for k in range(len(s4)-1,-1,-1):
    s5+=s4[k]
print(s5)

