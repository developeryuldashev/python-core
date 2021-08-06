a=[5,1,2,1,3,7,13,4,5,1,4,1,1]
# i=0
# while i>len(a):
#     t=a[i]
#     for j in range(i+1,len(a)):
#         if t==a[j]:
#             print(i,j,end=' ')
#             a.remove(a[j])

#a=[1,2,3,1,2,4,1]
d=[]
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]==a[j]:
            if (not i in d):
                d.append(i)
            if (not j in d):
                d.append(j)
d.sort()
print(d)