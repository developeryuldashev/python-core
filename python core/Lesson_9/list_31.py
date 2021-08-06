a=[2,1,6,5,3,4,5]
sanoq=0
b=[]
for i in range(len(a)-1,0,-1):
    if a[i]>a[i-1]:
        print(i,'\t',end='')
        sanoq+=1
print('sanoq=',sanoq)
    