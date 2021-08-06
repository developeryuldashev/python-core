# coding=utf-8
a = [5,1,2,1,3,7,1,2]
d = []
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]==a[j]:
            if not i in d:
                d.append(i)
            if not j in d:
                d.append(j)
d.sort()
print(d)