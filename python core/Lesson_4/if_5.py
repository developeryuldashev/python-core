a,b,c=0,-5,0
sanoq1=0
sanoq2=0
t=0
if a>0:
    sanoq1=sanoq1+1
elif a<0:
    sanoq2+=1
else:
    t+=1
if b>0:
    sanoq1+=1
elif b<0:
    sanoq2+=1
else:
    t+=1
if c>0:
    sanoq1+=1
elif c<0:
    sanoq2+=1
else:
    t+=1
print(f"musbat sonlar soni {sanoq1} va manfiy sonlar {sanoq2} va nollar soni{t}")