# coding=utf-8
a = [6,3,2,5,4,7,1]
b = a.copy()
b.sort()
c = 0
for i in range(len(a)):
    if a[i]!=b[i]:
        c += 1
if c%2==0:
    c = int(c/2)
else:
    c = int((c+1)/2)
print(a)
print(b)
print(c)